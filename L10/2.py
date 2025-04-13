import pygame
import random
import time
import psycopg2

pygame.init()


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",  
        user="postgres",     
        password="12345678"   
    )


def get_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT user_id, username FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user


def create_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return user_id


def get_user_level(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT level, score FROM users WHERE user_id = %s", (user_id,))
    level_score = cur.fetchone()
    conn.close()
    if level_score:
        return level_score
    else:
        return (1, 0) 

def save_game(user_id, level, score):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET level = %s, score = %s WHERE user_id = %s",
        (level, score, user_id)
    )
    conn.commit()
    conn.close()



class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  
        self.direction = (CELL_SIZE, 0)  

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)  
        self.body.pop() 

    def grow(self, weight):
        for _ in range(weight): 
            self.body.append(self.body[-1])

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True  
        if self.body[0] in self.body[1:]:
            return True 
        return False

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] and new_direction[1] != -self.direction[1]):
            self.direction = new_direction


class Food:
    def __init__(self, snake):
        self.position = self.generate_food(snake)
        self.weight = random.randint(1, 3)  
        self.spawn_time = time.time()  
        self.lifetime = random.randint(5, 10)  

    def generate_food(self, snake):
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def has_expired(self):
        return time.time() - self.spawn_time > self.lifetime 


def get_player_name():
    username = input("Enter your name: ")
    return username


def main():
    username = get_player_name()  
    user = get_user(username)
    
    if user is None:
        user_id = create_user(username)  
    else:
        user_id = user[0]  

    level, score = get_user_level(user_id)  

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake)
    running = True
    speed = 6

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((CELL_SIZE, 0))

        snake.move()

        if snake.body[0] == food.position:
            snake.grow(food.weight)
            score += food.weight
            food = Food(snake)

            if score % 3 == 0:
                level += 1
                speed += 2

        if food.has_expired():
            food = Food(snake)

        if snake.check_collision():
            running = False

        pygame.draw.rect(screen, RED, (*food.position, CELL_SIZE, CELL_SIZE))
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)

    save_game(user_id, level, score) 
    print(f"Saving: user_id={user_id}, level={level}, score={score}")

    pygame.quit()

if __name__ == "__main__":
    main()

