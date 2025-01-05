# MovieRez

A FastAPI-based movie reservation system.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## Available Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## API Documentation

Once the server is running, you can access:
- Interactive API docs at `http://localhost:8000/docs`
- Alternative API docs at `http://localhost:8000/redoc`
