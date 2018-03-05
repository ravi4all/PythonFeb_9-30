import pygame
import random

pygame.init()

red = 255,0,0
black = 0,0,0
yellow = 255,255,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255

size = width, height = 900, 500

colors = [black,yellow,green,black,white]
circle_color = random.choice(colors)

screen = pygame.display.set_mode(size)

ball = pygame.image.load('ball.jpg')

x = 0
y = 0

clock = pygame.time.Clock()
FPS = 100

move_x = 5
move_y = 8

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    # pygame.draw.circle(screen, circle_color, [x,y], 50)

    screen.blit(ball, (x,y))

    x += move_x
    y += move_y

    if x >= width - 225:
        move_x = -5
    elif y >= height - 225:
        move_y = -5
    elif x < 0:
        move_x = 5
    elif y < 0 :
        move_y = 5

    pygame.display.update()
    clock.tick(FPS)