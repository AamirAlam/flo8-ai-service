FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create directory for the database if it doesn't exist
RUN mkdir -p /app/db

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Use gunicorn as the production WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "wsgi:app"]
