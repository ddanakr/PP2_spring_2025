import psycopg2
import pygame
import random
from pygame.math import Vector2
import time

conn = psycopg2.connect(database = "postgres",
                        host = 'localhost',
                        user = "postgres",
                        password = "dana3262")



def create_table_users():

    command = """CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE
                )"""
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    except Exception as e:
        print("Error creating 'users' table:", e)

def create_table_userscore():

    command = """CREATE TABLE IF NOT EXISTS userscore (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    score INTEGER DEFAULT 0,
                    level INTEGER DEFAULT 1,
                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    except Exception as e:
        print("Error creating 'userscore' table:", e)


create_table_users()
create_table_userscore()


def get_user_id(username):

    command = """SELECT id FROM users WHERE username = %s"""

    with conn.cursor() as cur:
        cur.execute(command, (username,))
        user = cur.fetchone()
        conn.commit()
        if user:
            return user[0]
        else:
            command2 = """INSERT INTO users (username) VALUES (%s) RETURNING id"""
            

            with conn.cursor() as cur:
                cur.execute(command2, (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
            return new_id
        

def load_progress(user_id):

    command = """SELECT score, level FROM userscore WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1"""
    with conn.cursor() as cur:
        cur.execute(command, (user_id,))
        conn.commit()

        row = cur.fetchone()
        return row if row else (0,0)
    
def save_progress(user_id, score, level):
    command = """INSERT INTO userscore (user_id, score, level) VALUES (%s, %s, %s)"""

    with conn.cursor() as cur:
        cur.execute(command, (user_id, score, level))
        conn.commit()

    print(f"Progress saved: user_id={user_id}, score={score}, level={level}")




USERNAME = input("Enter your username: ")
USER_ID = get_user_id(USERNAME)
score, level = load_progress(USER_ID)


# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

# cell size for the grid
CELL = 30

# Colors
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorORANGE = (255, 165, 0)
colorGREED1 =  (220, 220, 200)
colorGREED2 = (140, 140, 125)


font1 = pygame.font.SysFont("Verdana", 60)
game_over_im = font1.render("GAME OVER", True, "black")
game_over_rect = game_over_im.get_rect(center = (WIDTH // 2, HEIGHT // 2))


# Score and Level counter
font2 = pygame.font.SysFont("Verdana", 20)
score_counter = font2.render(f"Score: {score}", True, "green")
score_counter_rect = score_counter.get_rect(center = (WIDTH - 100, 30))

font3 = pygame.font.SysFont("Verdana", 20)
level_counter = font3.render(f"Level: {level}", True, "green")
level_counter_rect = level_counter.get_rect(center = (WIDTH - 100, 50))




def get_level(score):
    if score < 500:
        return 0
    elif 500 <= score < 1000:
        return 1
    elif score >= 1000:
        return 2
    

def get_speed(level):
    if level == 0:
        return 150
    elif level == 1:
        return 125
    elif level == 2:
        return 100
    
def get_walls_for_level(level):
    walls = set()
    if level >= 0:
        for x in range(WIDTH // CELL):
            walls.add((x, 0))
            walls.add((x, WIDTH // CELL - 1))
        for y in range(HEIGHT // CELL):
            walls.add((0, y))
            walls.add((HEIGHT // CELL - 1, y))

    if level >= 1:
        for i in range(5, 10):
            walls.add((i, i))

    if level >= 2:
        for i in range(10, 20):
            walls.add((i, WIDTH // CELL - i))

    return walls









# Function to draw the chessboard grid
def draw_grid_chess():
    colors = [colorGREED1, colorGREED2]
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


# Fruit class to represent food for the snake
class Fruit:
    def __init__(self):
        self.pos = Vector2(-1, -1)
    def draw(self):
        # drawing a fruit
        fruit_rect = pygame.Rect(int(self.pos.x * CELL,), int(self.pos.y * CELL), CELL, CELL)
        pygame.draw.rect(screen, colorRED, fruit_rect)
    
    def randomize(self, snake_body):
         # Generate a random position for the fruit so it won't appear on the body of the snake
        while True:
            self.x = random.randint(1, WIDTH // CELL - 2)
            self.y = random.randint(1, HEIGHT // CELL - 2)
            self.pos = Vector2(self.x, self.y)

            if self.pos not in snake_body:
                break


# Snake class to move and draw it
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 6), Vector2(5, 7), Vector2(5,8)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def move(self):
        if self.new_block: # Add a new block if the snake has eaten a fruit
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

        # Move the snake by shifting positions
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def draw(self):
        # Draw the snake's head
        head = self.body[0]
        pygame.draw.rect(screen, colorORANGE, (int(head.x * CELL), int(head.y * CELL), CELL, CELL))
        # Draw the snake's body
        for block in self.body[1:]:
            x_pos = int(block.x * CELL)
            y_pos = int(block.y * CELL)
            pygame.draw.rect(screen, colorYELLOW, (x_pos, y_pos, CELL, CELL))

    
# Game speed to make it harder
speed = get_speed(level)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, speed)
level = get_level(score)
walls = get_walls_for_level(level)


# Main game logic
class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.fruit.randomize(self.snake.body)
    
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw()
        self.fruit.draw()

    def draw_walls(self):
        for wx, wy in walls:
            pygame.draw.rect(screen, "red", (wx*CELL, wy*CELL, CELL, CELL))

    # Check if the snake eats the fruit
    def check_collision(self):
        global score, level, speed, walls
        head = self.snake.body[0]
        if head == self.fruit.pos:
            self.fruit.randomize(self.snake.body)
            self.snake.new_block = True
            # Increase score
            score += 100
            new_level = get_level(score)
            if new_level != level:
                level = new_level
                speed = get_speed(level)
                walls = get_walls_for_level(level)
                for wx, wy in walls:
                    pygame.draw.rect(screen, "red", (wx*CELL, wy*CELL, CELL, CELL))
                pygame.time.set_timer(SCREEN_UPDATE, speed)
            
    
    def check_fail(self):
        walls = get_walls_for_level(level)
        #1 check walls
        for block in walls:
            if block == self.snake.body[0]:
                self.game_over()
        
        #2 Check if the snake collides with itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        save_progress(USER_ID, score, level)
        print(f" Score saved: {USERNAME}, {score}")

        global running
        running = False

        screen.fill("red")
        screen.blit(game_over_im, game_over_rect)
        pygame.display.flip()

        time.sleep(3)

    
        


main_game = Main()

paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(USER_ID, score, level)
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:  # moving the snake
            if event.key == pygame.K_UP and main_game.snake.direction.y == 0:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y == 0:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x == 0:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x == 0:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_p:
                    save_progress(USER_ID, score, level)

                    font = pygame.font.SysFont("Verdana", 60)

                    paused_text = font.render("Paused", True, "black")
                    paused_text_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                    paused = True
                    while paused:
                        screen.fill(colorYELLOW)
                        screen.blit(paused_text, paused_text_rect)

                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                save_progress(USER_ID, score, level)
                                pygame.quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    paused = False
                                elif event.key == pygame.K_q:
                                    save_progress(USER_ID, score, level)
                                    pygame.quit()
    

    # Draw the game elements
    draw_grid_chess()
    main_game.draw_elements()
    main_game.draw_walls()

    # Display score and level
    score_counter = font2.render(f"Score: {score}", True, "green")
    score_counter_rect = score_counter.get_rect(center = (WIDTH - 100, 30)) 
    screen.blit(score_counter, score_counter_rect)

    level_counter = font3.render(f"Level: {level}", True, "green")
    level_counter_rect = level_counter.get_rect(center = (WIDTH - 100, 50))
    screen.blit(level_counter, level_counter_rect)


    pygame.display.flip()
    clock.tick(FPS)


conn.close()