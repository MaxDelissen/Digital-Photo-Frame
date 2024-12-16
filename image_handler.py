import random
from io import BytesIO
import requests
from PIL import Image
import PhotoFetcher

def fetch_images(album_title, screen_width, screen_height, crop_images, random_pool, amount_of_recent_items):
    """Fetch marked images and random images from the album."""
    chosen_images = PhotoFetcher.get_marked_images_from_album(album_title, screen_width, screen_height, crop_images)
    chosen_images.extend(PhotoFetcher.get_random_images_from_album(album_title, random_pool, amount_of_recent_items, screen_width, screen_height, crop_images))
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

def fetch_and_process_image(image_url, screen_width, screen_height):
    """Fetch image from the URL and process it."""
    try:
        response = requests.get(image_url, timeout=10)
        img_data = Image.open(BytesIO(response.content))
        return scale_and_center_image(img_data, screen_width, screen_height)
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
        return None
