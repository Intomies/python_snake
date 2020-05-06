import pygame
import random
import re

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
def show_scores(display, msg, font_style, color, position):
    value = font_style.render(msg, True, color)
    display.blit(value, position)

# Check if highscorelist exists and return current highscore
# If the list doesn't exist, creates new list with higscore set to 0
def check_if_highscore_list_exists():
    hs_file = "hs.txt"
    try:
        f = open(hs_file, "r")
        f_contents = f.read()
        return int(re.findall(r"\b\d+\b", f_contents)[0])
    except:
        f = open(hs_file, "w")
        f.write("Highscore: " + str(0))
        f.close()
        f = open(hs_file, "r")
        f_contents = f.read()
        return int(re.findall(r"\b\d+\b", f_contents)[0])
    finally:
        f.close()

def check_if_new_highscore(player_score):
    hs_file = "hs.txt"
    f = open(hs_file, "r")
    f_contents = f.read()
    f.close()
    if int(re.findall(r"\b\d+\b", f_contents)[0]) < player_score:
        f = open(hs_file, "w")
        f.write("Highscore: " + str(player_score))
        f.close()
        return True
    else:
        return False

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