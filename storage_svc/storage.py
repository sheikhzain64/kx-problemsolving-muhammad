from flask import Flask, jsonify

app = Flask(__name__)
data = {"id": 1, "message": "Hello from Storage Service!"}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(host='0.0.0.0', port=port)
