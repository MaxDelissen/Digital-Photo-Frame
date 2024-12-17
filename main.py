import json
import threading
import pygame
import locale
from image_handler import fetch_images, fetch_and_process_image
from display_utils import display_welcome_message, display_error_message, render_clock_and_date
from video_utils import display_video

try:
    locale.setlocale(locale.LC_TIME, 'nl_NL')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'C')  # Fallback to the default locale

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

album_title = config['album_title']
random_pool = config['random_pool']
amount_of_recent_items = config['amount_of_recent_items']
display_duration = config['display_duration']
clock_size = config['clock_size']
date_size = config['date_size']
screen_width = config['screen_width']
screen_height = config['screen_height']
cropImages = config['cropImages']

loaded_images = []
image_loading_event = threading.Event()

def get_images():
    return fetch_images(album_title, screen_width, screen_height, cropImages, random_pool, amount_of_recent_items)

def load_images_in_background():
    global loaded_images
    loaded_images = get_images()
    image_loading_event.set()

def display_video_and_load_images(video_path):
    # Start the image loading thread
    image_loader_thread = threading.Thread(target=load_images_in_background)
    image_loader_thread.start()

    # Play the video while images are loading
    display_video(video_path)

def display_images():
    global loaded_images
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Full-screen window
    pygame.mouse.set_visible(False)  # Hide the mouse cursor

    clock_font = pygame.font.Font(None, clock_size)
    date_font = pygame.font.Font(None, date_size)
    font = pygame.font.Font(None, 72)

    # Start the image loading thread and play the boot video simultaneously
    display_video_and_load_images('boot.avi')

    display_welcome_message(screen, screen_width, screen_height, font)

    image_loading_event.wait()

    if not loaded_images:
        display_error_message(screen, screen_width, screen_height, font)

        # Wait for 10 seconds before exiting
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 10000:
            pygame.time.wait(100)
        return

    # Loop to display the images
    while True:
        for image_url in loaded_images:
            img_data = fetch_and_process_image(image_url, screen_width, screen_height)
            if img_data:
                # Convert image to pygame surface
                img_surface = pygame.image.fromstring(img_data.tobytes(), img_data.size, img_data.mode)

                # Display the image
                screen.blit(img_surface, (0, 0))
                pygame.display.flip()

                image_start_time = pygame.time.get_ticks()

                while pygame.time.get_ticks() - image_start_time < display_duration * 1000:
                    render_clock_and_date(screen, screen_width, screen_height, clock_font, date_font)
                    pygame.display.flip()
                    pygame.time.wait(100)

        # Reload the images after finishing displaying the first batch
        loaded_images = get_images()

    pygame.quit()

if __name__ == '__main__':
    try:
        display_images()
    except KeyboardInterrupt:
        pygame.quit()
