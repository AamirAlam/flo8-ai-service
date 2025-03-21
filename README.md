# Flask API Project

A Flask-based REST API with AI integration.

## Project Overview

This project is a Flask-based REST API that provides AI-related endpoints. It's designed with a modular structure using Flask Blueprints and includes Docker support for containerized deployment.

## Features

- RESTful API architecture
- CORS support for cross-origin requests
- AI endpoints
- Docker and Docker Compose support
- AWS deployment ready

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Docker and Docker Compose (optional, for containerized deployment)

## Installation and Setup

### Local Development Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

   The API will be available at `http://localhost:5001`

### Using Docker

1. Build and run using Docker Compose:
   ```
   docker-compose up --build
   ```

   The API will be available at `http://localhost:5001`

2. To run in detached mode:
   ```
   docker-compose up -d
   ```

3. To stop the containers:
   ```
   docker-compose down
   ```

## API Endpoints

- `GET /`: Welcome message
- `GET /api/ai/`: Returns a test AI response

## Project Structure

```
flask-api/
├── app/                    # Application package
│   ├── __init__.py         # Application factory
│   ├── config.py           # Configuration settings
│   └── routes/             # API routes
│       └── ai_routes.py    # AI-related endpoints
├── .gitignore              # Git ignore file
├── AWS_DEPLOYMENT_GUIDE.md # AWS deployment instructions
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── run.py                  # Development server entry point
└── wsgi.py                 # Production server entry point
```

## Deployment

For AWS deployment instructions, please refer to the [AWS Deployment Guide](AWS_DEPLOYMENT_GUIDE.md).

## Development

To add new routes, create new blueprint files in the `app/routes` directory and register them in `app/__init__.py`.

## License

[Your License Here]
