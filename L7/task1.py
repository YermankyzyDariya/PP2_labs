
import pygame
import time



pygame.init()


WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))



body = pygame.image.load("clock.png")
right_hand = pygame.image.load("min_hand.png")  
left_hand = pygame.image.load("sec_hand.png")   


body = pygame.transform.scale(body, (800, 800)).convert()
right_hand = pygame.transform.scale(right_hand, (750, 750)).convert()
left_hand = pygame.transform.scale(left_hand, (750, 750)).convert()
left_hand.set_colorkey((0, 0, 0)) 
right_hand.set_colorkey((0, 0, 0)) 
body.set_colorkey((0, 0, 0)) 
center_x, center_y = WIDTH // 2, HEIGHT // 2


running = True
while running:
    screen.fill((0, 0, 0))  

   
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

   
    angle_seconds = -seconds * 6  
    angle_minutes = -minutes * 6  

    
    body_rect = body.get_rect(center=(center_x, center_y))
    screen.blit(body, body_rect)

   
    left_hand_rotated = pygame.transform.rotate(left_hand, angle_seconds)
    left_rect = left_hand_rotated.get_rect(center=(center_x, center_y))
    screen.blit(left_hand_rotated, left_rect)

   
    right_hand_rotated = pygame.transform.rotate(right_hand, angle_minutes)
    right_rect = right_hand_rotated.get_rect(center=(center_x, center_y))
    screen.blit(right_hand_rotated, right_rect)

    
    pygame.display.flip()
    pygame.time.delay(1000)  
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
