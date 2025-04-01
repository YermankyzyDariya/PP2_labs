import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Начальные параметры
drawing = False  # Рисуем ли сейчас
last_pos = None  # Последняя позиция курсора
color = BLACK  # Цвет по умолчанию
radius = 5  # Толщина кисти

# Основной цикл
screen.fill(WHITE)  # Заливаем фон
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Выбор цвета по клавишам
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_c:
                screen.fill(WHITE)  # Очистка экрана
        
        # Начало рисования
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        
        # Окончание рисования
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        
        # Рисование линий
        elif event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.line(screen, color, last_pos, event.pos, radius)
            last_pos = event.pos

    pygame.display.flip()

pygame.quit()