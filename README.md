# KX Problem solving exercise

## Problem
We would like you to implement a distributed **Service Assembly** with a gateway component.

## Description
The service assembly will have the following components:
1) **Storage Service** - stores in-memory, dummy data that can be accessed through a REST GET call in JSON format
2) **Gateway Service** - main process that serves data to clients and tracks the availability of the Storage Services (there could be 0 to 3 available) and has the following REST endpoints
    * **/status** - returns the status of each Storage Service
    * **/data** - fetches the dummy data from a Storage Service (eg. with round robin) and returns the data in JSON format

We would like the services to be containerised and run with docker-compose.
The services can be implemented using any programming language.

## Architecture
<img src="https://user-images.githubusercontent.com/90027208/152865747-5c4734dd-c046-4170-ae04-f0ea1448cf89.png" width="300">

## Acceptance criteria
* Please fork this git repository and work inside your own
* Provide a solution for the described problem and give us the instructions necessary to execute it
* We would like to have your solution in form of a Pull Request into the main repository
* _What should the Gateway do if no Storage Services are running?_

## SOLUTION


## Architecture Overview

### Gateway Service
- Acts as an API Gateway/Load Balancer
- Handles incoming requests and routes them to appropriate storage services
- Implements simple round-robin load balancing
- Built with Python using Flask framework

### Storage Service
- Provides data storage and retrieval functionality
- Can be scaled horizontally with multiple instances
- Also built with Flask framework

## Technical Stack
- Python
- Flask (Web Framework)
- Docker & Docker Compose
- RESTful APIs

## Service Communication
- Services communicate via HTTP/REST
- Gateway implements load balancing for multiple storage service instances
- Health checks are implemented to ensure service availability

## Project Structure
```
.
├── docker-compose.yaml    # Docker compose configuration
├── gateway_svc/          # Gateway service
│   └── gateway.py        # Gateway implementation with load balancing
└── storage_svc/          # Storage service
    └── storage.py        # Storage implementation with data endpoint
```

## Setup and Deployment
1. Ensure Docker and Docker Compose are installed on your system
2. Clone this repository
3. Run `docker-compose up --build` on main directory to build and start the services
4. Verify the Setup Access the services using curl or your web browser:

    - Gateway Service Status: http://localhost:5000/status
    - Gateway service data( round robin): http://localhost:5000/data
    - Storage Service 1: http://localhost:5001/data
    - Storage Service 2: http://localhost:5002/data
    - Storage Service 3: http://localhost:5003/data

## API Endpoints

### Gateway Service
- `GET /status` - Health check endpoint that returns the status of all storage services
- `GET /data` - Retrieves data from storage services using round-robin load balancing

### Storage Service
- `GET /data` - Returns stored data with a simple JSON response

## Testing Endpoints

You can use the following `curl` commands to test the storage services:

### Gatway service accessing Storage Service

- curl http://localhost:5000/data
- Expected response: 
  {
    "id": 1,
    "message": "Hello from Storage Service!"
  }

### Storage Service 1

- curl http://localhost:5001/data . 
- Expected response: 
  {
    "id": 1,
    "message": "Hello from Storage Service!"
  }
### Storage Service 2

- curl http://localhost:5002/data . 
- Expected response: 
  {
    "id": 1,
    "message": "Hello from Storage Service!"
  }
### Storage Service 3

- curl http://localhost:5003/data . 
- Expected response: 
  {
    "id": 1,
    "message": "Hello from Storage Service!"
  }

### Gateway Service
- curl http://localhost:5000/status
- {"http://storage_svc_1:5001":"Available","http://storage_svc_2:5001":"Available","http://storage_svc_3:5001":"Available"}

## Load Balancing
The gateway service implements a round-robin load balancing strategy:
- Maintains a list of available storage services
- Rotates through services for each request
- Skips unavailable services automatically
- Returns 503 error if no services are available

## Error Handling
- Gateway implements timeouts (2 seconds) for storage service requests
- Provides appropriate error responses when services are unavailable
- Includes error logging for failed service communications

## Scaling
The architecture supports horizontal scaling of the storage service by adding more instances through Docker Compose. Currently configured with:
- 1 Gateway service (port 5000)
- Multiple Storage services (starting at port 5001)

## Network Configuration
Services communicate over a Docker network named 'gateway-network' which:
- Isolates the services from external networks
- Enables service discovery using Docker DNS
- Allows internal communication between services