# SSE Demo

A demonstration project showcasing Server-Sent Events (SSE) implementation. This project includes both Python and Node.js examples of SSE servers.

## Project Structure

```
.
├── python-sse-demo/
│ ├── app.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── docker-compose.yml
└── nodejs-sse-demo/
├── server.js
└── package.json
```

## Python Implementation

### Prerequisites

- Python 3.11+
- Flask
- Docker (optional)

### Running the Python Server

#### Without Docker:

```bash
python app.py
```

#### With Docker:

```bash
docker-compose up
```

The Python server will start on port 3000.

## Node.js Implementation

### Prerequisites

- Node.js
- Express

### Running the Node.js Server

```bash
npm start
```

The Node.js server will start on port 3000.

## API Endpoints

Both implementations provide the following endpoints:

- `GET /` - Test endpoint that returns "Server is running!"
- `GET /events` - SSE endpoint that sends continuous updates to the client

## Testing the SSE Connection
