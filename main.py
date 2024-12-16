import json
import pygame
import locale
from image_handler import fetch_images, fetch_and_process_image
from display_utils import display_welcome_message, display_error_message, render_clock_and_date

locale.setlocale(locale.LC_TIME, 'nl_NL')

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

def get_images():
    return fetch_images(album_title, screen_width, screen_height, cropImages, random_pool, amount_of_recent_items)

def display_images():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Full-screen window
    pygame.mouse.set_visible(False)  # Hide the mouse cursor

    clock_font = pygame.font.Font(None, clock_size)
    date_font = pygame.font.Font(None, date_size)
    font = pygame.font.Font(None, 72)

    display_welcome_message(screen, screen_width, screen_height, font)

    images = get_images()
    if not images:
        display_error_message(screen, screen_width, screen_height, font)

        # Wait for 10 seconds before exiting
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 10000:
            pygame.time.wait(100)
        return

    while True:
        for image_url in images:
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

        images = get_images()

    pygame.quit()

if __name__ == '__main__':
    try:
        display_images()
    except KeyboardInterrupt:
        pygame.quit()
