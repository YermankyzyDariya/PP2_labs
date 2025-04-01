import pygame
import random

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20  # Размер одного сегмента змейки
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Направления движения
UP = (0, -TILE_SIZE)
DOWN = (0, TILE_SIZE)
LEFT = (-TILE_SIZE, 0)
RIGHT = (TILE_SIZE, 0)

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Начальное положение змейки
        self.direction = RIGHT  # Начальное направление вправо
        self.grow = False  # Флаг, обозначающий, должна ли змейка увеличиваться

    def move(self):
        # Получаем текущие координаты головы змейки
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = (x + dx, y + dy)

        # Проверяем, не вышла ли змейка за границы экрана
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return False  # Игра окончена

        # Проверка на столкновение с самой собой
        if new_head in self.body:
            return False  # Игра окончена

        # Добавляем новую голову
        self.body.insert(0, new_head)

        # Если змейка не должна расти, удаляем последний сегмент
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True  # Игра продолжается

    def change_direction(self, new_direction):
        # Проверяем, чтобы змейка не развернулась в противоположную сторону
        if (self.direction[0] + new_direction[0], self.direction[1] + new_direction[1]) != (0, 0):
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True  # Активируем рост змейки

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, TILE_SIZE, TILE_SIZE))  # Отрисовка каждого сегмента змейки

# Класс еды
class Food:
    def __init__(self):
        self.position = self.generate_position()  # Генерация случайного положения еды

    def generate_position(self):
        return (random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
                random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, TILE_SIZE, TILE_SIZE))

# Инициализация игры
snake = Snake()
food = Food()
score = 0  # Переменная для хранения счета

clock = pygame.time.Clock()
running = True  # Переменная для контроля игрового цикла

while running:
    screen.fill(WHITE)  # Заполняем экран белым цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)
            elif event.key == pygame.K_r:  # Перезапуск игры при нажатии R
                snake = Snake()
                food = Food(snake)
                score = 0

    # Движение змейки
    if not snake.move():
        running = False  # Если змейка выходит за границы или врезается в себя, игра заканчивается

    # Проверка на поедание еды
    if snake.body[0] == food.position:
        snake.grow_snake()  # Увеличиваем длину змейки
        food = Food()  # Создаем новую еду
        score += 1  # Увеличиваем счет

    # Отрисовка объектов
    snake.draw()
    food.draw()

    # Отображение счета
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Обновляем экран
    clock.tick(10)  # Управляем скоростью игры

pygame.quit()