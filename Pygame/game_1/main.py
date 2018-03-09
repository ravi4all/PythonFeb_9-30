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

screen = pygame.display.set_mode(size)
apple = pygame.image.load("assets/apple.png")

apple_x = random.randint(0,width-54)
apple_y = random.randint(0,height-68)

coin_sound = pygame.mixer.Sound('assets/point.wav')
gameOverSound = pygame.mixer.Sound('assets/game_over.wav')

x = 0
y = 0

clock = pygame.time.Clock()
FPS = 100

move_x = 0
move_y = 0

snakeList = []
snakeLength = 0

snake_width = 50

counter = 0

def gameOver():
    font = pygame.font.SysFont(None, 80)
    text = font.render("Game Over", True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, [width/2 - 80, height/2-40])

        pygame.display.update()

def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score : "+str(counter), True, black)
    screen.blit(text, [10,10])

def snake(snakeList):
    for i in snakeList:
        pygame.draw.rect(screen, red, [i[0], i[1], 50, 50])

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 5
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -5
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 5
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -5
                move_x = 0

    screen.fill(white)
    screen.blit(apple, [apple_x, apple_y])
    rect_1 = pygame.draw.rect(screen, red, [x,y,50,50])
    rect_2 = pygame.Rect(apple_x, apple_y, apple.get_width(), apple.get_height())

    if rect_1.colliderect(rect_2):
        # print("Collision detection")
        apple_x = random.randint(0, width - 54)
        apple_y = random.randint(0, height - 68)
        # snake_width += 20
        snakeLength += 5
        counter += 1
        coin_sound.play()

    x += move_x
    y += move_y

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)

    snakeList.append(snakeHead)
    snake(snakeList)
    # print(snakeList)
    if len(snakeList)  > snakeLength:
        del snakeList[0]

    for each in snakeList[:-1]:
        if each == snakeList[-1]:
            # print("Game Over")
            gameOverSound.play()
            gameOver()

    score(counter)

    pygame.display.update()
    clock.tick(FPS)