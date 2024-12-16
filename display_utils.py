import pygame
from datetime import datetime

def render_message(screen, text, font, color, x, y):
    """Render and display a message on the screen."""
    message_surface = font.render(text, True, color)
    screen.blit(message_surface, (x, y))

def render_clock_and_date(screen, screen_width, screen_height, clock_font, date_font):
    """Render the clock and date on the screen."""
    current_time = datetime.now().strftime("%H:%M")
    current_date = datetime.now().strftime("%A, %d %B")

    # Render the clock and date
    clock_surface = clock_font.render(current_time, True, (255, 255, 255))
    date_surface = date_font.render(current_date, True, (255, 255, 255))

    # Position the clock and date in the bottom-right corner
    clock_x = screen_width - clock_surface.get_width() - 30
    clock_y = screen_height - clock_surface.get_height() - 30
    date_x = screen_width - date_surface.get_width() - 30
    date_y = clock_y - date_surface.get_height() - 20

    # Draw the clock and date
    screen.blit(clock_surface, (clock_x, clock_y))
    screen.blit(date_surface, (date_x, date_y))

def display_welcome_message(screen, screen_width, screen_height, font):
    """Display a welcome message on the screen."""
    welcome_text = font.render("De fotolijst wordt nu gestart, even geduld AUB", True, (255, 255, 255))
    sub_text = font.render("Max Delissen - 2024", True, (255, 255, 255))
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(welcome_text, (screen_width // 2 - welcome_text.get_width() // 2, screen_height // 3))
    screen.blit(sub_text, (screen_width // 2 - sub_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()

def display_error_message(screen, screen_width, screen_height, font):
    """Display an error message when no images are found."""
    error_text = font.render("Geen foto's gevonden. Herstart de stroom.", True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
