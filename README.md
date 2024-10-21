# Digital Photo Frame Project

## Overview
This project aims to create a simple, user-friendly digital photo frame that automatically displays pictures from a shared Google Photos album. It’s designed for non-technical users, requiring no interaction beyond plugging it in and turning it on. The frame will automatically connect to a pre-configured Wi-Fi network and display photos in a continuous slideshow.

### Key Features:
- **Google Photos Integration**: Pulls images from a specific shared album.
- **Automatic Boot and Slideshow**: The device auto-starts and runs the slideshow on boot.
- **Minimal User Interaction**: Only requires power on/off using a physical switch.
- **Automatic Display Control**: The screen turns off during set hours (e.g., nighttime).
- **Wi-Fi Pre-Configuration**: Connects to a specific Wi-Fi network without any setup needed by the user.

## Hardware Components:
- **Raspberry Pi 4** (or alternative microcontroller)
- **~30-inch Display** (Salvaged from an old laptop or bought separately)
- **Power supply**: 5V USB power supply with in-line switch
- **Micro SD card (32GB)**: For OS and program storage
- **Optional: 3D printed frame**: Holds the display and Raspberry Pi in place
- **HDMI cable**: Connects the Raspberry Pi to the display

## Software Stack:
- **Raspberry Pi OS**: Linux-based OS to run the frame.
- **Google Photos API**: To access and display images from the shared album.
- **Python or JavaScript**: To create the slideshow and control the frame’s functionality.
- **Pillow/Pygame (Python)** or **HTML/CSS/JavaScript** for image display.
- **Cron Jobs**: Automate display on/off at specific times.

## Steps to Build:
1. **Install Raspberry Pi OS** on the Raspberry Pi.
2. **Set up Wi-Fi**: Pre-configure `wpa_supplicant.conf` with Wi-Fi credentials.
3. **Google Photos API Setup**: Authenticate using OAuth 2.0 and set up access to the shared album.
4. **Create Slideshow Program**: A Python or web-based app that fetches images and displays them in fullscreen mode.
5. **Automatic Startup**: Configure the system to auto-login and launch the slideshow script on boot.
6. **Screen Power Control**: Set up scripts to turn the display on/off during specified hours (e.g., using `vcgencmd display_power`).

## Optional Customizations:
- 3D print a custom frame for the display.
- Use a physical power switch for ease of use.
- Add environmental sensors (e.g., ambient light sensor) to control brightness.
