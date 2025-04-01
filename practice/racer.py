import pygame
import random
import time
import os

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Функция загрузки изображений
def load_image(name, size=None):
    path = os.path.join(os.getcwd(), "practice", name)
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size) if size else image

# Загрузка ресурсов
background = load_image("AnimatedStreet.png")
player_img = load_image("Player.png")
enemy_img = [
    load_image("Enemy.png"),
    load_image("car1.png"),
    load_image("car2.png")
]
coin_img = load_image("coin.png", (30, 30))

# Музыка и звуки
pygame.mixer.music.load(os.path.join(os.getcwd(), "lab9", "racer", "background.wav"))
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "lab9", "racer", "crash.wav"))

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

# Игровые параметры
FPS = 60
clock = pygame.time.Clock()
PLAYER_SPEED = 5
ENEMY_SPEED = 5
COIN_SPEED = 4
score = 0
enemy_index = 0  # Индекс текущего врага

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

    def generate_random_rect(self):
        global enemy_index
        enemy_index = (enemy_index + 1) % len(enemy_img)  # Меняем индекс перед каждым появлением
        self.image = enemy_img[enemy_index]  # Меняем изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -random.randint(50, 150)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            global combo
            combo = 1  # Сброс комбо
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = -random.randint(50, 150)

# Создание объектов
player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

# Генерация первых монет
for _ in range(3):
    coin = Coin()
    all_sprites.add(coin)
    coin_sprites.add(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    player.move()
    enemy.move()
    
    for coin in coin_sprites:
        coin.move()

    # Отрисовка всех объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Проверка столкновения игрока и врага
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        pygame.time.delay(int(crash_sound.get_length() * 1000))
        screen.fill("red")
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Проверка столкновения с монетами
    collected_coins = pygame.sprite.spritecollide(player, coin_sprites, True)
    for coin in collected_coins:
        score += 1  
        new_coin = Coin()
        all_sprites.add(new_coin)
        coin_sprites.add(new_coin)

    # Отображение счета
    score_text = font_small.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 100, 10))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()