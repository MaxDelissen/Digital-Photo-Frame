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

# Install the required Python packages
echo "Installing required Python packages..."
pip3 install -r $PROJECT_PATH/requirements.txt

echo "All dependencies installed."