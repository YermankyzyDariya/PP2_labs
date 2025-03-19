import pygame


pygame.init()


WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)


current_color = BLACK
drawing = False
shape = "pencil"  
start_pos = None
last_pos = None


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "pencil"
            elif event.key == pygame.K_2:
                shape = "rect"
            elif event.key == pygame.K_3:
                shape = "circle"
            elif event.key == pygame.K_4:
                shape = "eraser"
            elif event.key == pygame.K_c:
                screen.fill(WHITE) 
            elif event.key in [pygame.K_r, pygame.K_g, pygame.K_b, pygame.K_k]:
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_k:
                    current_color = BLACK

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
            if shape in ["rect", "circle"]:
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                if shape == "rect":
                    pygame.draw.rect(screen, current_color, rect, 2)
                elif shape == "circle":
                    center = (start_pos[0] + rect.width // 2, start_pos[1] + rect.height // 2)
                    radius = min(abs(rect.width), abs(rect.height)) // 2
                    pygame.draw.circle(screen, current_color, center, radius, 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == "pencil":
                pygame.draw.line(screen, current_color, last_pos, event.pos, 2)
            elif shape == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, 10)
            last_pos = event.pos
    
    pygame.display.flip()
    
pygame.quit()