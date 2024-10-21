import json
import random
import time
from time import sleep

import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
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
    random.shuffle(chosen_images) # Shuffle the images so marked images are not always displayed first
    return chosen_images


def display_images():
    """Display images in a full-screen Tkinter window."""
    window = tk.Tk()
    window.title("Digital Photo Frame")

    # Set the window to full screen
    window.attributes("-fullscreen", True)  # Enable full-screen mode
    window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))  # Exit full screen on Escape key

    # Create a label to display the welcome message
    welcome_label = tk.Label(window, text=f"De fotolijst wordt nu gestart, even geduld AUB\n\nMax Delissen - 2024",
                             font=("Helvetica", 32), bg='black', fg='white', justify='center')
    welcome_label.pack(expand=True, fill=tk.BOTH)  # Make the label expand to fill the window

    # Update the window to show the message
    window.update()

    sleep(2)

    # Fetch images
    images = fetch_images()
    if not images:

        welcome_label.config(text="Geen foto's gevonden, probeer de stroom te herstarten.\n\n(Trek de stekker uit het stopcontact en steek hem er weer in.)")
        window.update()
        sleep(10)
        welcome_label.config(text="Het programma stopt nu, als dit probleem zich blijft voordoen, vraag dan om hulp.\n\n--Max")
        window.update()
        sleep(5)
        return

    # Remove loading message once images are fetched
    welcome_label.pack_forget()  # Hide the loading label

    # Create a label to display the images
    image_label = tk.Label(window)
    image_label.pack(expand=True, fill=tk.BOTH)  # Make the label expand to fill the window

    while True:
        for image_url in images:
            # Fetch the image data
            response = requests.get(image_url)
            img_data = Image.open(BytesIO(response.content))
            img = ImageTk.PhotoImage(img_data)

            # Update the label with the new image
            image_label.config(bg='black')
            image_label.config(image=img)
            image_label.image = img  # Keep a reference to avoid garbage collection
            window.update()  # Update the window
            time.sleep(display_duration)  # Wait for the display duration
        images = fetch_images()  # Fetch new images after displaying all images

    window.mainloop()

if __name__ == '__main__':
    display_images()
