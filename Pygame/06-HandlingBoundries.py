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

    screen.fill(red)

    pygame.draw.circle(screen, circle_color, [x,y], 50)

    x += move_x
    y += move_y

    if x >= width - 50:
        move_x = -5
        circle_color = random.choice(colors)
    elif y >= height - 50:
        move_y = -5
        circle_color = random.choice(colors)
    elif x < 50:
        move_x = 5
        circle_color = random.choice(colors)
    elif y < 50 :
        move_y = 5
        circle_color = random.choice(colors)

    pygame.display.update()
    clock.tick(FPS)