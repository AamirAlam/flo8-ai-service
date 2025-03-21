FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Use gunicorn as the production WSGI server
RUN pip install gunicorn

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "wsgi:app"]
