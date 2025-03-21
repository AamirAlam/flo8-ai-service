# AWS Deployment Guide for Flask API

This guide will walk you through deploying your Flask API on an AWS EC2 instance using Docker Compose.

## Prerequisites

1. An AWS account
2. An EC2 instance running Amazon Linux 2, Ubuntu, or other Linux distribution
3. SSH access to your EC2 instance

## Step 1: Set Up Your EC2 Instance

1. Launch an EC2 instance (t2.micro is sufficient for testing)
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
   mkdir flask-api
   # (From your local machine)
   scp -i your-key.pem -r /path/to/local/flask-api/* ec2-user@your-instance-public-dns:~/flask-api/
   ```

2. Navigate to your project directory:
   ```bash
   cd flask-api
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up -d
   ```

4. Verify the container is running:
   ```bash
   docker-compose ps
   ```

## Step 4: Test Your API

1. From your EC2 instance:
   ```bash
   curl http://localhost:5001/
   curl http://localhost:5001/api/items/
   ```

2. From your local machine:
   ```bash
   curl http://your-instance-public-dns:5001/
   curl http://your-instance-public-dns:5001/api/items/
   ```

## Step 5: Set Up Automatic Restart (Optional)

Configure Docker to start automatically when the instance reboots:

```bash
sudo systemctl enable docker
```

## Step 6: Set Up a Domain Name and HTTPS (Optional)

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

## Scaling and Production Considerations

For a production environment, consider:

1. Using AWS Elastic Container Service (ECS) or Elastic Kubernetes Service (EKS)
2. Setting up a load balancer
3. Using AWS RDS for database (if applicable)
4. Implementing proper monitoring with CloudWatch
5. Setting up CI/CD pipelines for automated deployment
