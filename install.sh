#!/bin/bash

# Prompt for Service name
read -p "Enter the Service name: " SERVICE_NAME

# Set the Project path to the current directory
PROJECT_PATH=$(pwd)

# Define the executable
EXECUTABLE="python3 $PROJECT_PATH/main.py"  # Replace 'main.py' with your script's entry point

# Update the system package list
echo "Updating package list..."
sudo apt update -y

# Install Python3 and pip (if not already installed)
echo "Installing Python3 and pip..."
sudo apt install python3 python3-pip -y

# Install Tkinter for Python3 (for GUI)
echo "Installing Tkinter..."
sudo apt install python3-tk -y

# Install PIL (Python Imaging Library)
echo "Installing Pillow (PIL)..."
pip3 install --no-cache-dir --index-url https://pypi.org/simple Pillow

# Install requests (for fetching images from the web)
echo "Installing requests..."
pip3 install --no-cache-dir --index-url https://pypi.org/simple requests

# Install prerequisite packages for Google API libraries
echo "Installing prerequisite libraries for Google API client..."
sudo apt install build-essential libssl-dev libffi-dev python3-dev -y

# Install Google API client libraries (Google Auth and OAuthlib)
echo "Installing Google API client libraries..."
pip3 install --no-cache-dir --index-url https://pypi.org/simple --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Verify installation
echo "Verifying installations..."
python3 -c "import tkinter; import requests; import PIL; import googleapiclient; import google.auth; print('All dependencies are installed successfully!')"

echo "All dependencies installed. Setting up systemd service..."

# Create a systemd service file
sudo bash -c "cat > /etc/systemd/system/$SERVICE_NAME.service" <<EOL
[Unit]
Description=Digital Photo Frame Service
After=network.target

[Service]
ExecStart=$EXECUTABLE
WorkingDirectory=$PROJECT_PATH
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
EOL

# Set the proper permissions for the service file
sudo chmod 644 /etc/systemd/system/$SERVICE_NAME.service

# Reload systemd to recognize the new service
echo "Reloading systemd..."
sudo systemctl daemon-reload

# Enable the service to start on boot
echo "Enabling the service to start at boot..."
sudo systemctl enable $SERVICE_NAME

# Start the service
echo "Starting the service..."
sudo systemctl start $SERVICE_NAME

# Check the status of the service
sudo systemctl status $SERVICE_NAME

echo "Service setup complete! Your project will now start on boot."
