import pygame

pygame.init()
HEIGHT = 600
WIDTH = 800
RADIUS = 25
x , y = HEIGHT // 2 , WIDTH // 2
STEP = 20
screen = pygame.display.set_mode((WIDTH , HEIGHT))
COLOR_RED = (255 , 0 , 0)
running = True
while running:
    screen.fill((255 , 255 , 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()       
    if keys[pygame.K_UP] and y - RADIUS - STEP >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + RADIUS + STEP <= HEIGHT:
        y += STEP
    if keys[pygame.K_LEFT] and x - RADIUS - STEP >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + RADIUS + STEP <= WIDTH:
        x += STEP



   
    circle = pygame.draw.circle(screen , COLOR_RED , (x , y) , RADIUS)
    pygame.display.flip()
    pygame.time.delay(30)



pygame.quit()