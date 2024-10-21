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

echo "All dependencies installed. You can now run your project!"
