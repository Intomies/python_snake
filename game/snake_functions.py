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
    mess_rect = mess.get_rect(center = (display_w / 2, display_h / 2))
    display.blit(mess, mess_rect)

# Draws the snake on display
def draw_snake(brick_size, snake_container, snake_color, display):
    for i in snake_container:
        pygame.draw.rect(display, snake_color, [i[0], i[1], brick_size, brick_size])

# Renders the score on display
def show_score(display, score, font_style, color):
    value = font_style.render('Score: ' + str(score), True, color)
    display.blit(value, [0,0])

# Larger hit area for food
def check_food_hit(snake_pos_x, snake_pos_y, food_pos_x, food_pos_y, food_size):
    hit_area = food_size/2
    # Left
    if snake_pos_x == food_pos_x - hit_area and snake_pos_y == food_pos_y:
        return True
    # Right
    if snake_pos_x == food_pos_x + hit_area and snake_pos_y == food_pos_y:
        return True
    # Up
    if snake_pos_y == food_pos_y - hit_area and snake_pos_x == food_pos_x:
        return True
    # Down
    if snake_pos_y == food_pos_y + hit_area and snake_pos_x == food_pos_x:
        return True