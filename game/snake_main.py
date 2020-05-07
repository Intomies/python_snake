import pygame
import random
import time
import snake_functions as sf

class Brick():
    def __init__(self, color, size, pos_x, pos_y):
        self.color = color
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y

class Snake(Brick): 
    def __init__(self, color, size, pos_x, pos_y, speed_x, speed_y, game_speed, length):
        Brick.__init__(self, color, size, pos_x, pos_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.game_speed = game_speed
        self.length = length

class Food(Brick):
     def __init__(self, color, size, pos_x, pos_y, exists):
        Brick.__init__(self, color, size, pos_x, pos_y)
        self.exists = exists

def main():

    # Stylings
    font_style_head = pygame.font.SysFont('Consolas', 52)
    font_style_basic = pygame.font.SysFont('Consolas', 24)
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

    # Clock and movement speed settings
    clock = pygame.time.Clock()
    clock_speed = 20
    move_speed = 5

    # Snake settings
    snake_container = []
    _snake = Snake(
                red, 
                brick_size, 
                int(display_w/2), 
                int(display_h/2), 
                move_speed, 
                0, 
                clock_speed,
                1
                )
   
    # Food settings
    _food = Food(
                sf.random_color(), 
                brick_size, 
                sf.random_position(display_w, brick_size), 
                sf.random_position(display_h, brick_size), 
                True
                )
    
    # Scores
    highscore = sf.check_if_highscore_list_exists()
    new_highscore = False
    player_score = 0
    
    # Game screen control
    main_game_on = True
    starting_screen = True
    game_over_screen = False

    # Main game loop
    while main_game_on:

        # Displays the starting-screen
        while starting_screen:
            
            display.fill(display_background)
            
            sf.show_message(
                        'SNAKE', 
                        green, 
                        display,
                        display_w,
                        display_h - 100,
                        font_style_head
                        )
            sf.show_message(
                        '(n)ew, (q)uit', 
                        red, 
                        display,
                        display_w,
                        display_h + 100,
                        font_style_basic
                        )
            
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
            
            if new_highscore:
                clock.tick(3)
                sf.show_message(
                            'NEW HIGHSCORE!',
                            sf.random_color(), 
                            display,
                            display_w,
                            display_h - 100,
                            font_style_head
                            )
            
            sf.show_message(
                        'Game Over! Your Score: ' + str(player_score), 
                        red, 
                        display,
                        display_w,
                        display_h,
                        font_style_basic
                        )
            sf.show_message(
                        '(q)uit', 
                        red, 
                        display,
                        display_w,
                        display_h + 100,
                        font_style_basic
                        )
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
            
            if e.type == pygame.QUIT:
                starting_screen = False
                game_over_screen = False
                main_game_on = False

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
                    new_highscore = sf.check_if_new_highscore(player_score)
        
        # Snakes movement. Head is in separate array so that it can be checked if it hits the tail 
        _snake.pos_x += _snake.speed_x
        _snake.pos_y += _snake.speed_y
        snake_head = []
        snake_head.append(_snake.pos_x)
        snake_head.append(_snake.pos_y)
        snake_container.append(snake_head)
        
        display.fill(display_background)

        # This sends snake to the other side of the screen if it goes over displayed area
        if _snake.pos_x >= display_w:
            _snake.pos_x = 0
        if _snake.pos_x < 0:
            _snake.pos_x = display_w
        if _snake.pos_y >= display_h:
            _snake.pos_y = 0
        if _snake.pos_y < 0:
            _snake.pos_y = display_h

        # This draws the food. If it gets eaten, creates a new one with new color and position.
        if _food.exists:
            pygame.draw.rect(display,_food.color,[int(_food.pos_x),int(_food.pos_y),_food.size,_food.size])
        else:
            _food.color = (sf.random_color())
            _food.pos_x = sf.random_position(display_w, _food.size)
            _food.pos_y = sf.random_position(display_h, _food.size)
            _food.exists = True

        # This checks if the food gets eaten. If it does, player gets a point and every 5 points the game gets faster.
        if sf.check_food_hit(_snake.pos_x, _snake.pos_y, _food.pos_x, _food.pos_y, _food.size):
            _snake.color = _food.color
            _snake.length += 1
            _food.exists = False
            player_score += 1
            if player_score % 5 and player_score != 0:
                _snake.game_speed += 1

        # This keeps up snakes length
        if len(snake_container) > _snake.length:
            del snake_container[0]
        
        # This checks if the snakes head hits its tail. If it does, checks if playr score is a new highscore and launches the Game Over-screen 
        for i in snake_container[:-1]:
            if i == snake_head:
                game_over_screen = True
                new_highscore = sf.check_if_new_highscore(player_score)
        
        # This draws the snake and shows scores on display
        sf.draw_snake(_snake.size, snake_container, _snake.color, display)
        sf.show_scores(display, ('Score: ' + str(player_score)), font_style_basic, red, [0,0])
        sf.show_scores(display, ('Highscore: ' + str(highscore)), font_style_basic, blue, [0,25])

        # These keep everything animated
        pygame.display.update()
        clock.tick(_snake.game_speed)

    
    quit()


if __name__ == "__main__": 
    pygame.init()
    sf.check_if_highscore_list_exists()
    main()
    pygame.quit()

