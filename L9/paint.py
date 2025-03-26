import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров экрана и цветов
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# Текущий цвет и инструмент рисования
current_color = BLACK
shape = "pencil"  # Инструмент по умолчанию
start_pos = None
last_pos = None

drawing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Выбор инструмента
            if event.key == pygame.K_1:
                shape = "pencil"
            elif event.key == pygame.K_2:
                shape = "rect"
            elif event.key == pygame.K_3:
                shape = "circle"
            elif event.key == pygame.K_4:
                shape = "eraser"
            elif event.key == pygame.K_5:
                shape = "square"
            elif event.key == pygame.K_6:
                shape = "right_triangle"
            elif event.key == pygame.K_7:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_8:
                shape = "rhombus"
            
            # Очистка экрана
            elif event.key == pygame.K_c:
                screen.fill(WHITE)
            
            # Смена цвета
            elif event.key == pygame.K_r:
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
            end_pos = event.pos
            
            if shape in ["rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                
                if shape == "rect":
                    pygame.draw.rect(screen, current_color, rect, 2)
                elif shape == "square":
                    side = min(abs(rect.width), abs(rect.height))
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side), 2)
                elif shape == "circle":
                    center = (start_pos[0] + rect.width // 2, start_pos[1] + rect.height // 2)
                    radius = min(abs(rect.width), abs(rect.height)) // 2
                    pygame.draw.circle(screen, current_color, center, radius, 2)
                elif shape == "right_triangle":
                    pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
                elif shape == "equilateral_triangle":
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, current_color, [
                        (start_pos[0], start_pos[1] + height),
                        (start_pos[0] + height, start_pos[1] + height),
                        (start_pos[0] + height // 2, start_pos[1])
                    ], 2)
                elif shape == "rhombus":
                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2
                    width = abs(end_pos[0] - start_pos[0]) // 2
                    height = abs(end_pos[1] - start_pos[1]) // 2
                    pygame.draw.polygon(screen, current_color, [
                        (center_x, start_pos[1]),
                        (end_pos[0], center_y),
                        (center_x, end_pos[1]),
                        (start_pos[0], center_y)
                    ], 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == "pencil":
                pygame.draw.line(screen, current_color, last_pos, event.pos, 2)
            elif shape == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, 10)
            last_pos = event.pos
    
    pygame.display.flip()

pygame.quit()