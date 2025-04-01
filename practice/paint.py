#paint

import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint: Кривая и Выравнивание")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Переменные
drawing = False
points = []

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Начало рисования
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            points = [event.pos]

        # Добавление точек к линии
        elif event.type == pygame.MOUSEMOTION and drawing:
            points.append(event.pos)

        # Окончание рисования
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Выравнивание линии по горизонтали (ENTER)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if points:
                avg_y = sum(y for _, y in points) // len(points)  # Средняя высота
                points = [(x, avg_y) for x, _ in points]  # Все точки на одной высоте

    # Рисование линии
    if len(points) > 1:
        pygame.draw.lines(screen, BLACK, False, points, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

