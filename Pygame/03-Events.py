import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((900,500))

screen.fill(red)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(screen, black, [10,10,50,50])
    pygame.draw.circle(screen,black,[100,100],80)

    pygame.display.update()