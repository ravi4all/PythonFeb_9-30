import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((900,500))

screen.fill(red)

pygame.draw.rect(screen, black, [10,10,50,50])

pygame.display.update()
