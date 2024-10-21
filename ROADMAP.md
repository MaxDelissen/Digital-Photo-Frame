# Digital Photo Frame Roadmap

## Phase 1: Research and Design
- [ ] Research display options (~30 inches). Check availability and viability of using a salvaged laptop display.
- [ ] Confirm power requirements for Raspberry Pi and display.
- [ ] Research alternatives to Raspberry Pi if needed (lower cost/more performance).

## Phase 2: Hardware Setup
- [ ] Purchase or salvage necessary hardware components.
- [ ] 3D print or build a frame for the display and Raspberry Pi.
- [ ] Connect display to Raspberry Pi (HDMI).
- [ ] Solder and attach a physical power switch.
- [ ] Test powering the Raspberry Pi and display together.

## Phase 3: Software Development
- [ ] Install Raspberry Pi OS on the microSD card.
- [ ] Configure auto-login and boot script.
- [ ] Pre-configure Wi-Fi (`wpa_supplicant.conf`).
- [ ] Set up Google Photos API integration (OAuth 2.0 authentication).
- [ ] Develop the slideshow program (Python or web-based).
- [ ] Test fetching and displaying images from the Google Photos album.

## Phase 4: User Experience
- [ ] Add script to control screen power based on time of day (e.g., turn off at night).
- [ ] Optimize the program for boot time (reduce delay in starting slideshow).
- [ ] Set up final configuration for non-technical users (auto-connect to Wi-Fi, auto-boot slideshow).

## Phase 5: Final Testing and Deployment
- [ ] Run extended tests to ensure Wi-Fi auto-connect and display behavior works as intended.
- [ ] Package the system for easy deployment (add setup instructions for power supply and switch).
- [ ] Deliver the frame to its intended user and ensure it works as expected.
