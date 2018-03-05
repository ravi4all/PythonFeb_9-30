import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((900,500))

x = 0
y = 0

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)

    pygame.draw.rect(screen, black, [x,y,50,50])

    x += 5
    y += 5

    pygame.display.update()
    clock.tick(FPS)