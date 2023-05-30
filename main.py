import pygame
from pygame.locals import *
from sys import exit
from random import randint
from settings import *

pygame.init()
screen = pygame.display.set_mode((width, height))

# Define screen name
pygame.display.set_caption('Snake game')

#Setting background music
background_music = pygame.mixer.music.load('BoxCat Games - Battle (Boss).mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#collision with apple sound
collision = pygame.mixer.Sound("smw_coin.wav")

#Set font to the game
font = pygame.font.SysFont('arial', 20, True, True)

def reset_game():
    global points, initial_lenght, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, isDead
    points = 0
    initial_lenght = 5
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    snake_list = []
    head_list = []
    x_apple = randint(50, 590)
    y_apple = randint(50, 430)
    isDead = False

def increase_snake(snake_list):
    for x_y in snake_list:
        pygame.draw.rect(screen, green_color, (x_y[0], x_y[1], 20, 20))

def set_snake_motion(event_key, x_control_method, y_control_method):
    if event_key == K_a:
        if x_control_method == velocity:
            pass
        else:
            x_control_method = -velocity
            y_control_method = 0
    if event_key == K_d:
        if x_control_method == -velocity:
            pass
        else:
            x_control_method = velocity
            y_control_method = 0
    if event_key == K_w:
        if y_control_method == velocity:
            pass
        else:
            y_control_method = -velocity
            x_control_method = 0
    if event_key == K_s:
        if y_control_method == -velocity:
            pass
        else:
            y_control_method = velocity
            x_control_method = 0
    return x_control_method, y_control_method

def check_snake_border_collision():
    global x_snake, y_snake, width, height
    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake > height:
        y_snake = 0
    if y_snake < 0:
        y_snake = height

def check_auto_collision():
    global event, isDead
    if snake_list.count(head_list) > 1:
        secondFont = pygame.font.SysFont('arial', 20, True, True)
        gameOverMessage = f'Game Over! Pressione a tecla R para jogar novamente'
        gameOverPointsMessage = f'Total de pontos: {points}'
        gameOverFormattedText = secondFont.render(gameOverMessage, True, white_color)
        gameOverPointsFormattedText = secondFont.render(gameOverPointsMessage, True, white_color)
        rect_Text = gameOverFormattedText.get_rect()
        rect_Points_Text = gameOverPointsFormattedText.get_rect()
        isDead = True
        while isDead:
            screen.fill(black_color)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reset_game()
            rect_Text.center = (width//2, height//2)
            rect_Points_Text.center = (width // 2, (height// 2)+20)
            screen.blit(gameOverFormattedText, rect_Text)
            screen.blit(gameOverPointsFormattedText, rect_Points_Text)
            pygame.display.update()

while True:
    clock.tick(30)
    screen.fill(black_color)
    message = f'Pontos: {points}'
    formatted_text = font.render(message, False, white_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            x_control, y_control = set_snake_motion(event.key, x_control, y_control)

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control
    square_side = 20
    snake = pygame.draw.rect(screen, green_color, (x_snake, y_snake, square_side, square_side))
    apple = pygame.draw.rect(screen, red_color, (x_apple, y_apple, square_side, square_side))

    if snake.colliderect(apple):
        x_apple = randint(50, 590)
        y_apple = randint(50, 430)
        points = points + 1
        collision.play()
        initial_lenght = initial_lenght + 5

    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)
    snake_list.append(head_list)
    increase_snake(snake_list)

    check_auto_collision()
    check_snake_border_collision()

    if len(snake_list) > initial_lenght:
        del snake_list[0]

    #text position on screen
    screen.blit(formatted_text, (440, 5))
    pygame.display.update()

    #another way to get keyboard input
    '''
        if pygame.key.get_pressed()[K_a]:
            x_snake = x_snake - 5
        if pygame.key.get_pressed()[K_d]:
            x_snake = x_snake + 5
        if pygame.key.get_pressed()[K_w]:
            y_snake = y_snake - 5
        if pygame.key.get_pressed()[K_s]:
            y_snake = y_snake + 5
        '''