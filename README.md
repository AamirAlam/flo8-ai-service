# Flask API Project

A Flask-based REST API with AI integration.

## Project Overview

This project is a Flask-based REST API that provides AI-related endpoints. It's designed with a modular structure using Flask Blueprints and includes Docker support for containerized deployment.

## Features

- RESTful API architecture
- CORS support for cross-origin requests
- OpenAI integration for AI capabilities
- LanceDB for vector storage and retrieval
- Docker and Docker Compose support
- AWS deployment ready
- Python 3.13 compatibility with workarounds

## Prerequisites

- Python 3.8+ (3.13 recommended)
- pip (Python package manager) or uv (recommended for Python 3.13)
- Docker and Docker Compose (optional, for containerized deployment)

## Installation and Setup

### Local Development Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-api
   ```

2. Set up your environment variables:
   ```
   # Run the environment setup script
   ./set_env.sh YOUR_OPENAI_API_KEY
   ```

3. Choose your installation method:

   #### Option 1: Using pip with venv
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

   #### Option 2: Using uv (recommended for Python 3.13)
   ```bash
   # Install uv if you don't have it
   pip install uv
   
   # Set up environment and install dependencies
   ./run_with_uv.sh
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
- `POST /api/ai/query`: Sends a query to the AI service and returns a response

### Example API Usage

```bash
# Query the AI service
curl -X POST http://localhost:5001/api/ai/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What is machine learning?"}'
```

## Project Structure

```
flask-api/
├── app/                    # Application package
│   ├── __init__.py         # Application factory
│   ├── config.py           # Configuration settings
│   ├── routes/             # API routes
│   │   └── ai_routes.py    # AI-related endpoints
│   └── ai-service/         # AI service components
│       ├── agent_run.py    # OpenAI integration
│       └── lancedb_setup.py # Vector database setup
├── .gitignore              # Git ignore file
├── .env                    # Environment variables (created by set_env.sh)
├── .env.example            # Example environment variables
├── AWS_DEPLOYMENT_GUIDE.md # AWS deployment instructions
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── run.py                  # Development server entry point
├── run_with_uv.sh          # Script to run with uv package manager
├── set_env.sh              # Script to set up environment variables
└── wsgi.py                 # Production server entry point
```

## Python 3.13 Compatibility

This project includes workarounds for Python 3.13 compatibility:

- The `tiktoken` package is not compatible with Python 3.13, so a fallback chunking mechanism is implemented
- Using `uv` as the package manager is recommended for Python 3.13 to resolve dependency conflicts

## Deployment

For AWS deployment instructions, please refer to the [AWS Deployment Guide](AWS_DEPLOYMENT_GUIDE.md).

## Development

To add new routes, create new blueprint files in the `app/routes` directory and register them in `app/__init__.py`.

## License

[Your License Here]
