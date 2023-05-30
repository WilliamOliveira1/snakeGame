import pygame
from random import randint

white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)
red_color = (255, 0, 0)

# screen size init
width = 640
height = 480

#snake init position
x_snake = int(width/2)
y_snake = int(height/2)

#apple init position
x_apple = randint(50, 590)
y_apple = randint(50, 430)

points = 0
velocity = 3
x_control = velocity
y_control = 0
isDead = False

#increase snake size
snake_list = []
initial_lenght = 5

clock = pygame.time.Clock()