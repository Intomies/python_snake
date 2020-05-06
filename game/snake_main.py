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
    font_size = 32
    font_style = pygame.font.SysFont(None, font_size)
    red = (255,0,0)
    blue = (50,50,255)
    black = (0,0,0)
    brick_size = 10

    # Display settings
    display_w = 500
    display_h = 500
    display_background = (black)
    display = pygame.display.set_mode((display_w,display_h))
    pygame.display.set_caption('Snake')

    # Movement speed settings
    clock = pygame.time.Clock()
    clock_speed = 20
    move_speed = 5

    # Snake settings
    snake_container = []
    start_x = int(display_w/2)
    start_y = int(display_h/2)
    _snake = Snake(
                red, 
                brick_size, 
                start_x, 
                start_y, 
                move_speed, 
                0, 
                clock_speed,
                1
                )
    # Food settings
    food_color = sf.random_color()
    _food = Food(
                food_color, 
                brick_size, 
                sf.random_position(display_w, brick_size), 
                sf.random_position(display_h, brick_size), 
                True
                )

    # Game init
    highscore = sf.check_if_highscore_list_exists()
    new_highscore = False
    score = 0
    game_on = True
    game_over = False

    # Game loop
    while game_on:

        while game_over:
            
            display.fill(black)
            
            if new_highscore:
                sf.show_message(
                        'Game Over! NEW HIGHSCORE: ' + str(score), 
                        red, 
                        display,
                        display_w,
                        display_h,
                        font_style
                        )
            else:
                sf.show_message(
                            'Game Over! Your Score: ' + str(score), 
                            red, 
                            display,
                            display_w,
                            display_h,
                            font_style
                            )
            sf.show_message(
                        '(q)uit, (n)ew', 
                        red, 
                        display,
                        display_w,
                        display_h + 100,
                        font_style
                        )
            pygame.display.update()

            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    game_on = False
                    game_over = False

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        game_on = False
                        game_over = False
                    if e.key == pygame.K_n:
                        main()

        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                game_on = False

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
                if e.key == pygame.K_q:
                    game_over = True
                    new_highscore = sf.check_if_new_highscore(score)
        
        _snake.pos_x += _snake.speed_x
        _snake.pos_y += _snake.speed_y
        display.fill(display_background)

        if _snake.pos_x >= display_w:
            _snake.pos_x = 0
        if _snake.pos_x < 0:
            _snake.pos_x = display_w
        if _snake.pos_y >= display_h:
            _snake.pos_y = 0
        if _snake.pos_y < 0:
            _snake.pos_y = display_h

        if _food.exists:
            pygame.draw.rect(display,_food.color,[int(_food.pos_x),int(_food.pos_y),_food.size,_food.size])
        else:
            _food.color = (sf.random_color())
            _food.pos_x = sf.random_position(display_w, _food.size)
            _food.pos_y = sf.random_position(display_h, _food.size)
            _food.exists = True
        
        snake_head = []
        snake_head.append(_snake.pos_x)
        snake_head.append(_snake.pos_y)
        snake_container.append(snake_head)

        if len(snake_container) > _snake.length:
            del snake_container[0]
        
        for i in snake_container[:-1]:
            if i == snake_head:
                game_over = True
                new_highscore = new_highscore = sf.check_if_new_highscore(score)
        
        sf.draw_snake(_snake.size, snake_container, _snake.color, display)
        sf.show_scores(display, ('Score: ' + str(score)), font_style, red, [0,0])
        sf.show_scores(display, ('Highscore: ' + str(highscore)), font_style, blue, [0,25])

        pygame.display.update()
        
        if sf.check_food_hit(_snake.pos_x, _snake.pos_y, _food.pos_x, _food.pos_y, _food.size):
            _snake.color = _food.color
            _snake.length += 1
            _food.exists = False
            score += 1
            if score % 5 and score != 0:
                _snake.game_speed += 1
        
        clock.tick(_snake.game_speed)

    
    quit()


if __name__ == "__main__": 
    pygame.init()
    sf.check_if_highscore_list_exists()
    main()
    pygame.quit()

