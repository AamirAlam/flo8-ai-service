# AWS Deployment Guide for Flask API

This guide will walk you through deploying your Flask API on an AWS EC2 instance using Docker Compose.

## Prerequisites

1. An AWS account
2. An EC2 instance running Amazon Linux 2, Ubuntu, or other Linux distribution
3. SSH access to your EC2 instance

## Step 1: Set Up Your EC2 Instance

1. Launch an EC2 instance (t2.micro is sufficient for testing, t2.small or larger recommended for production)
2. Configure security groups to allow:
   - SSH (port 22) from your IP
   - HTTP (port 80) from anywhere
   - HTTPS (port 443) from anywhere
   - Custom TCP (port 5001) from anywhere (or restrict as needed)
3. Create and download your key pair (.pem file)
4. Connect to your instance:
   ```
   chmod 400 your-key.pem
   ssh -i your-key.pem ec2-user@your-instance-public-dns
   ```

### Key Pair Issues

If you encounter issues with your key pair or need to add a new key pair to an existing EC2 instance:

1. **If you still have access to the instance**:
   ```bash
   # Generate a new key pair locally
   ssh-keygen -t rsa -b 2048 -f ~/.ssh/my-new-key
   
   # Copy the public key to the instance
   ssh -i original-key.pem ec2-user@your-instance-ip "mkdir -p ~/.ssh"
   cat ~/.ssh/my-new-key.pub | ssh -i original-key.pem ec2-user@your-instance-ip "cat >> ~/.ssh/authorized_keys"
   
   # Test the new key
   ssh -i ~/.ssh/my-new-key ec2-user@your-instance-ip
   ```

2. **If you don't have access**:
   - Stop the instance (don't terminate)
   - Create an AMI from the instance
   - Launch a new instance from the AMI with a new key pair
   - Assign the same Elastic IP (if applicable)

## Step 2: Install Docker and Docker Compose

### For Amazon Linux 2:
```bash
# Update packages
sudo yum update -y

# Install Docker
sudo amazon-linux-extras install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Log out and log back in for group changes to take effect
exit
# (reconnect via SSH)
```

### For Ubuntu:
```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ubuntu

# Install Docker Compose
sudo apt install docker-compose -y

# Log out and log back in for group changes to take effect
exit
# (reconnect via SSH)
```

## Step 3: Deploy Your Flask API

1. Clone your repository or upload your files to the EC2 instance:
   ```bash
   # If using git
   git clone your-repository-url
   
   # Or create a directory and upload files using SCP
   mkdir -p ~/ai-service
   # (From your local machine)
   scp -i your-key.pem -r /path/to/local/flask-api/* ec2-user@your-instance-public-dns:~/ai-service/
   ```

2. Navigate to your project directory:
   ```bash
   cd ~/ai-service
   ```

3. Set up environment variables:
   ```bash
   # Run the environment setup script
   ./set_env.sh YOUR_OPENAI_API_KEY
   ```

4. Build and start the Docker containers:
   ```bash
   docker-compose up -d
   ```

5. Verify the container is running:
   ```bash
   docker-compose ps
   ```

## Step 4: Manual Deployment (Without Docker)

If you prefer to run the application directly on the instance:

1. Install Python 3.8+ (3.13 recommended):
   ```bash
   # For Amazon Linux 2
   sudo yum install python3 python3-pip -y
   
   # For Ubuntu
   sudo apt install python3 python3-pip -y
   ```

2. Install uv (optional, recommended for Python 3.13):
   ```bash
   # Install uv
   pip install uv
   ```

3. Set up a virtual environment and install dependencies:
   ```bash
   # Navigate to your project directory
   cd ~/ai-service
   
   # Create and activate virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies with pip
   pip install -r requirements.txt
   
   # OR install with uv (recommended for Python 3.13)
   uv pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Run the environment setup script
   ./set_env.sh YOUR_OPENAI_API_KEY
   ```

5. Run the application:
   ```bash
   python3 run.py
   ```

## Step 5: Test Your API

1. From your EC2 instance:
   ```bash
   curl http://localhost:5001/
   curl http://localhost:5001/api/ai/query -X POST -H "Content-Type: application/json" -d '{"query":"Hello, how are you?"}'
   ```

2. From your local machine:
   ```bash
   curl http://your-instance-public-dns:5001/
   curl http://your-instance-public-dns:5001/api/ai/query -X POST -H "Content-Type: application/json" -d '{"query":"Hello, how are you?"}'
   ```

## Step 6: Set Up Automatic Restart (Optional)

Configure Docker to start automatically when the instance reboots:

```bash
sudo systemctl enable docker
```

For manual deployment, set up a systemd service:

```bash
sudo nano /etc/systemd/system/flask-api.service
```

Add the following content:

```
[Unit]
Description=Flask API Service
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/ai-service
ExecStart=/home/ec2-user/ai-service/venv/bin/python run.py
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable flask-api
sudo systemctl start flask-api
```

## Step 7: Set Up a Domain Name and HTTPS (Optional)

1. Register a domain name with Route 53 or another domain registrar
2. Set up an A record pointing to your EC2 instance's public IP
3. Install and configure Nginx as a reverse proxy
4. Set up SSL with Let's Encrypt

## Troubleshooting

1. Check container logs:
   ```bash
   docker-compose logs
   ```

2. Check if the container is running:
   ```bash
   docker ps
   ```

3. Check if the port is open:
   ```bash
   sudo netstat -tulpn | grep 5001
   ```

4. Check EC2 security groups to ensure port 5001 is open

5. Python 3.13 Compatibility Issues:
   - The project includes a workaround for tiktoken which isn't compatible with Python 3.13
   - If you encounter other compatibility issues, consider using Python 3.11 or 3.12

## Scaling and Production Considerations

For a production environment, consider:

1. Using AWS Elastic Container Service (ECS) or Elastic Kubernetes Service (EKS)
2. Setting up a load balancer
3. Using AWS RDS for database (if applicable)
4. Implementing proper monitoring with CloudWatch
5. Setting up CI/CD pipelines for automated deployment
