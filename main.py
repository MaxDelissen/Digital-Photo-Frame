import json
import random
import time
from io import BytesIO

import requests
from PIL import Image
import pygame
import PhotoFetcher

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

album_title = config['album_title']
random_pool = config['random_pool']
amount_of_recent_items = config['amount_of_recent_items']
display_duration = config['display_duration']
screen_width = config['screen_width']
screen_height = config['screen_height']
cropImages = config['cropImages']

print(album_title)

def fetch_images():
    """Fetch marked images and random images from the album."""
    chosen_images = PhotoFetcher.get_marked_images_from_album(album_title, screen_width, screen_height, cropImages)
    chosen_images.extend(PhotoFetcher.get_random_images_from_album(album_title, random_pool, amount_of_recent_items, screen_width, screen_height, cropImages))
    random.shuffle(chosen_images)  # Shuffle the images so marked images are not always displayed first
    return chosen_images

def scale_and_center_image(img, screen_width, screen_height):
    """Scale an image to fit within the screen while preserving aspect ratio and adding black borders."""
    img_width, img_height = img.size

    # Calculate scale to fit within the screen dimensions
    scale_w = screen_width / img_width
    scale_h = screen_height / img_height
    scale = min(scale_w, scale_h)

    # Compute new dimensions
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)

    # Resize the image
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)

    # Create a black background (padded surface)
    black_bg = Image.new("RGB", (screen_width, screen_height), (0, 0, 0))

    # Center the resized image on the black background
    x_offset = (screen_width - new_width) // 2
    y_offset = (screen_height - new_height) // 2
    black_bg.paste(resized_img, (x_offset, y_offset))

    return black_bg


def display_images():
    """Display images in full screen using pygame."""
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Full-screen window
    pygame.mouse.set_visible(False)  # Hide the mouse cursor

    # Display a welcome message
    font = pygame.font.Font(None, 72)
    screen.fill((0, 0, 0))  # Fill the screen with black
    welcome_text = font.render("De fotolijst wordt nu gestart, even geduld AUB", True, (255, 255, 255))
    sub_text = font.render("Max Delissen - 2024", True, (255, 255, 255))
    screen.blit(welcome_text, (screen_width // 2 - welcome_text.get_width() // 2, screen_height // 3))
    screen.blit(sub_text, (screen_width // 2 - sub_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    time.sleep(2)

    # Fetch images
    images = fetch_images()
    if not images:
        # Display an error message if no images are found
        error_text = font.render("Geen foto's gevonden. Herstart de stroom.", True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, screen_height // 2))
        pygame.display.flip()
        time.sleep(10)
        return

    # Main loop to display images
    while True:
        for image_url in images:
            try:
                # Fetch the image data
                response = requests.get(image_url, timeout=10)
                img_data = Image.open(BytesIO(response.content))

                # Scale and center the image on a black background
                img_data = scale_and_center_image(img_data, screen_width, screen_height)

                # Convert the image to a pygame surface
                img_surface = pygame.image.fromstring(img_data.tobytes(), img_data.size, img_data.mode)

                # Display the image
                screen.blit(img_surface, (0, 0))
                pygame.display.flip()

                # Wait for the display duration
                time.sleep(display_duration)

            except requests.RequestException as e:
                print(f"Error fetching image: {e}")
                continue

            # Refresh the image list after displaying all images
        images = fetch_images()

    # Quit pygame gracefully
    pygame.quit()

if __name__ == '__main__':
    try:
        display_images()
    except KeyboardInterrupt:
        pygame.quit()
