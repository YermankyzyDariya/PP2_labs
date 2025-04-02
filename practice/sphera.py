import pygame
import math

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Segment = pygame.image.load("segment.png")
Segment_small = pygame.image.load("segment_small.png")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


BIG_RADIUS = 50  
SMALL_RADIUS = 10  
Segment = pygame.transform.scale(Segment, (BIG_RADIUS * 2, BIG_RADIUS * 2))
Segment_small = pygame.transform.scale(Segment_small, (SMALL_RADIUS * 2, SMALL_RADIUS * 2))
CENTER = (WIDTH // 2, HEIGHT // 2)  
orbit_radius = 100  
angle = 0  
speed = 0.02  

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 0.01 
            elif event.key == pygame.K_DOWN:
                speed -= 0.01 
    
     # Вычисление позиции маленькой сферы
    small_x = CENTER[0] + orbit_radius * math.cos(angle)
    small_y = CENTER[1] + orbit_radius * math.sin(angle)
    angle += speed
    
  
    screen.blit(Segment, (CENTER[0] - BIG_RADIUS, CENTER[1] - BIG_RADIUS))  # Центрируем изображение
    screen.blit(Segment_small, (small_x - SMALL_RADIUS, small_y - SMALL_RADIUS))  # Маленький объект на орбите
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()