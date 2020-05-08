import pygame
import random
import time
import re

pygame.init()

# Stylings
font_style_head = pygame.font.SysFont('OCR A Extended', 52)
font_style_basic = pygame.font.SysFont('OCR A Extended', 24)
red = (255,0,0)
green = (0,255,0)
blue = (50,50,255)
black = (0,0,0)
brick_size = 10

# Display settings
display_w = 500
display_h = 500
display_background = (black)
display = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Snake')


# Basic graphical game object
class Brick():
    def __init__(self, color, size, pos_x, pos_y):
        self.color = color
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y


# Snake object that inherits from Brick-class
class Snake(Brick): 
    def __init__(self, color, size, pos_x, pos_y, speed_x, speed_y, game_speed, length, container):
        Brick.__init__(self, color, size, pos_x, pos_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.game_speed = game_speed
        self.length = length
        self.container = container

    # Grows snake and changes its color when it eats food
    def grow(self, food_color):
        self.color = food_color
        self.length += 1
    
    # Snakes movement. Head is in separate array so that it can be checked if it hits the tail.
    def move(self, snake_head):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        snake_head.append(self.pos_x)
        snake_head.append(self.pos_y)
        self.container.append(snake_head)

    # This sends snake to the other side of the screen if it goes over displayed area.
    def check_position(self, display_w, display_h):
        if self.pos_x >= display_w:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = display_w
        if self.pos_y >= display_h:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = display_h

    # Draws the snake on display
    def draw(self, display):
        for i in self.container:
            pygame.draw.rect(display, self.color, [i[0], i[1], brick_size, brick_size])


# Food object that inherits from Brick-class
class Food(Brick):
    def __init__(self, color, size, pos_x, pos_y, exists):
        Brick.__init__(self, color, size, pos_x, pos_y)
        self.exists = exists
        self.hit_area = self.size/2

    # Spawns new food when it get eaten
    def spawn(self):
        self.color = random_color()
        self.pos_x = random_position(display_w, self.size)
        self.pos_y = random_position(display_h, self.size)
        self.exists = True

    # Gives the food a bigger hit area
    def hit(self, snake_pos_x, snake_pos_y):
        # Left
        if snake_pos_x == self.pos_x - self.hit_area and snake_pos_y == self.pos_y:
            return True
        # Right
        if snake_pos_x == self.pos_x + self.hit_area and snake_pos_y == self.pos_y:
            return True
        # Up
        if snake_pos_y == self.pos_y - self.hit_area and snake_pos_x == self.pos_x:
            return True
        # Down
        if snake_pos_y == self.pos_y + self.hit_area and snake_pos_x == self.pos_x:
            return True

    # Draws the food on display
    def draw(self, display):
        pygame.draw.rect(display,self.color,[int(self.pos_x),int(self.pos_y),self.size,self.size])


# This is the class for all in game texts
class TextDisplay():
    def __init__(self, text, font_style, color, position, curr_score):
        self.text = text
        self.font_style = font_style
        self.color = color
        self.position = position
        self.curr_score = curr_score

    # Draws basic texts on display
    def draw_message(self, display):
        value = self.font_style.render(self.text, True, self.color)
        value_rect = value.get_rect(center = self.position)
        display.blit(value, value_rect)
    
    # Draws score-texts on display
    def draw_score(self, display):
        value = self.font_style.render(self.text + str(self.curr_score), True, self.color)
        value_rect = value.get_rect(center = self.position)
        display.blit(value, value_rect)

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

# Check if highscorelist exists and return current highscore
# If the list doesn't exist, creates new list with higscore set to 0
def check_if_highscore_list_exists():
    hs_file = 'hs.txt'
    try:
        f = open(hs_file, 'r')
        f_contents = f.read()
        return int(re.findall(r"\b\d+\b", f_contents)[0])
    except:
        f = open(hs_file, 'w')
        f.write('Highscore: ' + str(0))
        f.close()
        f = open(hs_file, 'r')
        f_contents = f.read()
        return int(re.findall(r'\b\d+\b', f_contents)[0])
    finally:
        f.close()

# Checks if players score is bigger than current highscore, and sets it to be if so.
def check_if_new_highscore(player_score):
    hs_file = 'hs.txt'
    f = open(hs_file, 'r')
    f_contents = f.read()
    f.close()
    if int(re.findall(r'\b\d+\b', f_contents)[0]) < player_score:
        f = open(hs_file, 'w')
        f.write('Highscore: ' + str(player_score))
        f.close()
        return True
    else:
        return False

def main():

    # Clock and movement speed settings
    clock = pygame.time.Clock()
    clock_speed = 20
    move_speed = 5

    # Snake settings
    _snake = Snake(
        red, 
        brick_size, 
        int(display_w/2), 
        int(display_h/2), 
        move_speed, 
        0, 
        clock_speed,
        1,
        []
    )
   
    # Food settings
    _food = Food(
        random_color(), 
        brick_size, 
        random_position(display_w, brick_size), 
        random_position(display_h, brick_size), 
        True
    )
    
    # Scores display settings
    new_highscore = False
    _player = TextDisplay(
        ('Score: '),
        font_style_basic,
        red,
        [display_w/2,25],
        0
    )
    _curr_highscore = TextDisplay(
        ('Highscore: '),
        font_style_basic,
        blue,
        [int(display_w)/2,50],
        check_if_highscore_list_exists()
    )

    # Messages/Game texts settings
    _m_title = TextDisplay(
        'SNAKE',
        font_style_head,
        green,
        [int(display_w/2),int(display_h/2 - 100)],
        0  
    )
    _m_game_over = TextDisplay(
        'Game Over! Your Score: ' + str(_player.curr_score),
        font_style_basic,
        red,
        [int(display_w/2),int(display_h/2)],
        0
    )
    _m_buttons = TextDisplay(
        '(n)ew | (q)uit',
        font_style_basic,
        red,
        [int(display_w/2),int(display_h/2 + 100)],
        0
    )
    _m_highscore = TextDisplay(
        'NEW HIGHSCORE!',
        font_style_head,
        random_color(),
        [int(display_w/2),int(display_h/2 - 100)], 
        0  
    )
    
    # Game screen control
    main_game_on = True
    starting_screen = True
    game_over_screen = False

    # Main game loop
    while main_game_on:

        # Sets the displays background color
        display.fill(display_background)

        # Displays the starting-screen
        while starting_screen:
            
            display.fill(display_background)
            
            _m_title.draw_message(display)
            _m_buttons.draw_message(display)
            
            for e in pygame.event.get():

                # Quit by closing screen
                if e.type == pygame.QUIT:
                    starting_screen = False
                    game_over_screen = False
                    main_game_on = False

                if e.type == pygame.KEYDOWN:
                    
                    # Quit game with q-key
                    if e.key == pygame.K_q or e.key == pygame.K_ESCAPE:
                        starting_screen = False
                        game_over_screen = False
                        main_game_on = False
                    
                    # New game with n-key
                    if e.key == pygame.K_n:
                        starting_screen = False
            
            pygame.display.update()
        
        # Displays the Game Over-screen
        while game_over_screen:
            
            display.fill(display_background)
            
            # If player get new highscore, this message gets drawn on display
            if new_highscore:
                clock.tick(3)
                _m_highscore.draw_message(display)
                _m_highscore.color = random_color()

            # Basic Game Over-text and players end score. Also button hint-text.
            _m_game_over.text = 'Game Over! Your Score: ' + str(_player.curr_score)
            _m_buttons.text = '(q)uit'
            _m_game_over.draw_message(display)
            _m_buttons.draw_message(display)
            pygame.display.update()

            for e in pygame.event.get():

                # Quit by closing game window
                if e.type == pygame.QUIT:
                    starting_screen = False
                    game_over_screen = False
                    main_game_on = False

                if e.type == pygame.KEYDOWN:
                    
                    # Quit with q-key
                    if e.key == pygame.K_q or e.key == pygame.K_ESCAPE:
                        main()

        # Snake controls
        for e in pygame.event.get():
            
            # Quits the game if display window is closed
            if e.type == pygame.QUIT:
                starting_screen = False
                game_over_screen = False
                main_game_on = False

            # Control keys
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and _snake.speed_x != move_speed:
                    _snake.speed_x = move_speed * -1
                    _snake.speed_y = 0
                if e.key == pygame.K_RIGHT and _snake.speed_x != move_speed * -1:
                    _snake.speed_x = move_speed
                    _snake.speed_y = 0
                if e.key == pygame.K_UP and _snake.speed_y != move_speed:
                    _snake.speed_x = 0
                    _snake.speed_y = move_speed * -1
                if e.key == pygame.K_DOWN and _snake.speed_y != move_speed * -1:
                    _snake.speed_x = 0
                    _snake.speed_y = move_speed
                if e.key == pygame.K_q or e.key == pygame.K_ESCAPE:
                    game_over_screen = True
                    new_highscore = check_if_new_highscore(_player.curr_score)
        
        # Snakes movement
        snake_head = []
        _snake.move(snake_head)        
        _snake.check_position(display_w, display_h)

        # This draws the food. If it gets eaten, creates a new one with new color and position.
        if _food.exists:
            _food.draw(display)
        else:
            _food.spawn()

        # This checks if the food gets eaten. If it does, player gets a point and every 5 points the game gets faster.
        if _food.hit(_snake.pos_x, _snake.pos_y):
            _snake.grow(_food.color)
            _food.exists = False
            _player.curr_score += 1
            if _player.curr_score % 5 and _player.curr_score != 0:
                _snake.game_speed += 1

        # This keeps track of the snakes length
        if len(_snake.container) > _snake.length:
            del _snake.container[0]
        
        # This checks if the snakes head hits its tail. 
        # If it does, checks if player score is a new highscore and launches the Game Over-screen 
        for i in _snake.container[:-1]:
            if i == snake_head:
                game_over_screen = True
                new_highscore = check_if_new_highscore(_player.curr_score)
        
        # This draws the snake and shows scores on display.
        _snake.draw(display)
        _player.draw_score(display)
        _curr_highscore.draw_score(display)
        
        # These keep everything moving on screen.
        pygame.display.update()
        clock.tick(_snake.game_speed)

    # Quits the game when main loop is broken.
    quit()


if __name__ == "__main__": 
    check_if_highscore_list_exists()
    main()
    pygame.quit()

