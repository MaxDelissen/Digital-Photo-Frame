#!/bin/bash

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
pip3 install Pillow

# Install requests (for fetching images from the web)
echo "Installing requests..."
pip3 install requests

# Install Google API client libraries (Google Auth and OAuthlib)
echo "Installing Google API client libraries..."
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Install any other dependencies for the project
echo "Installing additional Python dependencies..."
pip3 install random time

# Verify installation
echo "Verifying installations..."
python3 -c "import tkinter; import requests; import PIL; import googleapiclient; import google.auth; print('All dependencies are installed successfully!')"

echo "All dependencies installed. You can now run your project!"
