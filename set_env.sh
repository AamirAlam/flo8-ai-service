#!/bin/bash

# Check if API key is provided
if [ -z "$1" ]; then
  echo "Usage: ./set_env.sh YOUR_OPENAI_API_KEY"
  echo "This will create a .env file with your API key and other configuration."
  exit 1
fi

# Create or update .env file
cat > .env << EOL
# OpenAI API Key - Required for AI functionality
OPENAI_API_KEY=$1

# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_PORT=5001
EOL

echo ".env file created successfully with your API key."
echo "You can now run the application with: python3 run.py"

