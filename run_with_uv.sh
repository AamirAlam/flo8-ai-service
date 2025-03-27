#!/bin/bash

# Check if .venv directory exists
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment with uv..."
  uv venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if dependencies are installed
if [ ! -f ".venv/.dependencies_installed" ]; then
  echo "Installing dependencies with uv..."
  uv pip install -r requirements.txt
  touch .venv/.dependencies_installed
fi


# Run the Flask application
echo "Dependencies installed successfully. 🎉"
echo "👷🏻 Configure .env by running ./set_env.sh YOUR_OPENAI_API_KEY"
echo "Run the application with: python3 run.py"

