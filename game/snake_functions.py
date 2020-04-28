import pygame
import random

# Returns a random position on display
def random_position(d_x, size):
    return round(random.randrange(0, d_x - size) / 10.0) * 10.0

# Returns a random RGB color
def random_color():
    return (int((random.randrange(10, 255) / 10.0) * 10.0),
            int((random.randrange(10, 255) / 10.0) * 10.0),
            int((random.randrange(10, 255) / 10.0) * 10.0))

# Constructs attributes for message
def show_message(msg, color, display, display_w, display_h, font_style):
    mess = font_style.render(msg, True, color)
    display.blit(mess, [display_w / 20, display_h / 2])

# Draws the snake on display
def draw_snake(snake_size, snake_parts, snake_color, display):
    for i in snake_parts:
        pygame.draw.rect(display, snake_color, [i[0], i[1], snake_size, snake_size])

    


