import requests
from flask import Flask, jsonify

app = Flask(__name__)
storage_services = [
    "http://storage_svc_1:5001",
    "http://storage_svc_2:5001",
    "http://storage_svc_3:5001",
]


current_index = 0

def get_next_storage_service():
    global current_index
    if len(storage_services) == 0:
        return None
    service = storage_services[current_index]
    current_index = (current_index + 1) % len(storage_services)
    return service

@app.route('/status', methods=['GET'])
def status():
    statuses = {}
    for service in storage_services:
        try:
            response = requests.get(f"{service}/data", timeout=2)
            statuses[service] = "Available" if response.status_code == 200 else "Unavailable"
        except Exception as e:
            statuses[service] = "Unavailable"
            print(f"Error checking {service}: {e}")
    return jsonify(statuses), 200


@app.route('/data', methods=['GET'])
def data():
    if all(
        requests.get(f"{service}/data", timeout=2).status_code != 200 
        for service in storage_services
    ):
        return jsonify({"error": "No storage services available"}), 503
    for _ in range(len(storage_services)):
        service = get_next_storage_service()
        try:
            response = requests.get(f"{service}/data", timeout=2)
            if response.status_code == 200:
                return jsonify(response.json()), 200
        except Exception as e:
            print(f"Error contacting {service}: {e}")

    return jsonify({"error": "All storage services failed to respond"}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
