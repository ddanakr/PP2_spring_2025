import pygame
import random
from pygame.math import Vector2
import time

pygame.init()


WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

CELL = 30

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
colorORANGE = (255, 165, 0)
colorGREEN1 =  (220, 220, 200)
colorGREEN2 = (140, 140, 125)

font1 = pygame.font.SysFont("Verdana", 60)
game_over_im = font1.render("GAME OVER", True, "black")
game_over_rect = game_over_im.get_rect(center = (WIDTH // 2, HEIGHT // 2))

#fruits
score = 0
font2 = pygame.font.SysFont("Verdana", 20)
score_counter = font2.render(f"Score: {score}", True, "green")
score_counter_rect = score_counter.get_rect(center = (WIDTH - 100, 30))

level = 1
font3 = pygame.font.SysFont("Verdana", 20)
level_counter = font3.render(f"Level: {level}", True, "green")
level_counter_rect = level_counter.get_rect(center = (WIDTH - 100, 50))


def draw_grid_chess():
    colors = [colorGREEN1, colorGREEN2]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Fruit:
    def __init__(self):
        self.pos = Vector2(-1, -1)
    def draw(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL,), int(self.pos.y * CELL), CELL, CELL)
        pygame.draw.rect(screen, colorRED, fruit_rect)
    
    def randomize(self, snake_body):
        while True:
            self.x = random.randint(0, WIDTH // CELL - 1)
            self.y = random.randint(0, HEIGHT // CELL - 1)
            self.pos = Vector2(self.x, self.y)

            if self.pos not in snake_body:
                break



class Snake:
    def __init__(self):
        self.body = [Vector2(10, 11), Vector2(10, 12), Vector2(10,13)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorORANGE, (int(head.x * CELL), int(head.y * CELL), CELL, CELL))
        for block in self.body[1:]:
            x_pos = int(block.x * CELL)
            y_pos = int(block.y * CELL)
            pygame.draw.rect(screen, colorYELLOW, (x_pos, y_pos, CELL, CELL))

    

speed = 150
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, speed)

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

    def check_collision(self):
        global score, level, speed
        head = self.snake.body[0]
        if head == self.fruit.pos:
            self.fruit.randomize(self.snake.body)
            self.snake.new_block = True
            score += 100
            if score % 300 == 0:
                level += 1
                if speed >= 50:
                    speed -= 15
                pygame.time.set_timer(SCREEN_UPDATE, speed)
            
    
    def check_fail(self):
        #1
        if not 0 <= self.snake.body[0].x < WIDTH // CELL or not 0 <= self.snake.body[0].y < HEIGHT // CELL:
            self.game_over()
        #2
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        global running
        running = False

        screen.fill("red")
        screen.blit(game_over_im, game_over_rect)
        pygame.display.flip()

        time.sleep(3)

        


main_game = Main()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y == 0:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y == 0:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x == 0:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x == 0:
                main_game.snake.direction = Vector2(1, 0)
    
    draw_grid_chess()

    main_game.draw_elements()

    score_counter = font2.render(f"Score: {score}", True, "green")
    score_counter_rect = score_counter.get_rect(center = (WIDTH - 100, 30))
    screen.blit(score_counter, score_counter_rect)

    level_counter = font3.render(f"Level: {level}", True, "green")
    level_counter_rect = level_counter.get_rect(center = (WIDTH - 100, 50))
    screen.blit(level_counter, level_counter_rect)


    pygame.display.flip()
    clock.tick(FPS)