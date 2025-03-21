import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#load images
image_player = pygame.image.load("resources/Player.png")
image_enemy = pygame.image.load("resources/Enemy.png")
image_road = pygame.image.load("resources/AnimatedStreet.png")

image_coin = pygame.image.load("resources/coin.png")
image_coin = pygame.transform.scale(image_coin, (50, 50))


#load music and sounds
pygame.mixer.music.load("resources/background.wav")
sound_crach = pygame.mixer.Sound("resources/crash.wav")
sound_coin = pygame.mixer.Sound("resources/coin_sound.wav")
sound_game_over = pygame.mixer.Sound("resources/game_over.mp3")

pygame.mixer.music.play(-1)

# Define fonts and text
font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over!", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))


# Set up game clock
clock = pygame.time.Clock()
FPS = 60

running = True


# Define game parameters
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = random.randint(5, 10)


# Coin counter
earned_coins = 0
font2 = pygame.font.SysFont("Verdana", 20)
coin_counter = font2.render(f"Coins: {earned_coins}", True, "red")
coin_counter_rect = coin_counter.get_rect(center = (WIDTH - 100, 32))


#Player class
class Player(pygame.sprite.Sprite):
        def __init__(self):
              super().__init__()
              self.image = image_player
              self.rect = self.image.get_rect()
              self.rect.centerx = WIDTH // 2  # position of the car
              self.rect.bottom = HEIGHT
        
        def move(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]: # move left
                     self.rect.move_ip(-PLAYER_SPEED, 0)
                if keys[pygame.K_RIGHT]: # move right
                     self.rect.move_ip(PLAYER_SPEED, 0)
                if self.rect.left < 0:
                       self.rect.left = 0  
                if self.rect.right > WIDTH:
                       self.rect.right = WIDTH    

# Enemy class
class Enemy(pygame.sprite.Sprite):
        def __init__(self):
              super().__init__()
              self.image = image_enemy
              self.rect = self.image.get_rect() 
              self.generate_rand_rect()

        def generate_rand_rect(self):
               self.rect.left = random.randint(0, WIDTH - self.rect.w) #generate an enemy car in random position on the top
               self.rect.bottom = 0

        def move(self):
               self.rect.move_ip(0, ENEMY_SPEED) # moves downwards
               if self.rect.top > HEIGHT:  # Reset enemy position when it leaves the screen
                      self.generate_rand_rect()
              

# Coin class
class Coin(pygame.sprite.Sprite):
        def __init__(self):
              super().__init__()
              self.image = image_coin
              self.rect = self.image.get_rect()
              self.generate_rand_rect()
              self.respawn_time = 0
              self.next_spawn_delay = random.randint(4000, 7000) #set random spawnin delay
        
        def generate_rand_rect(self):
              self.rect.left = random.randint(0, WIDTH - self.rect.w) #generate coin on random position on the top
              self.rect.bottom = 0
        
        def move(self):
               if pygame.time.get_ticks()  < self.respawn_time:
                      return

               self.rect.move_ip(0, COIN_SPEED) #moves downwards
               if self. rect.top > HEIGHT: # Respawn coin after delay
                      self.respawn_time = pygame.time.get_ticks() + self.next_spawn_delay
                      self.generate_rand_rect()


# Game objects
enemy = Enemy()
player = Player()
coin = Coin()

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# Add objects to sprite groups
all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        #move player
        player.move()

        #draw background
        screen.blit(image_road, (0, 0))

        #update and display coin counter
        coin_counter = font2.render(f"Coins: {earned_coins}", True, "red")
        screen.blit(coin_counter, coin_counter_rect)
        
        
        # Move and draw all game objects
        for entity in all_sprites:
               entity.move()
               screen.blit(entity.image, entity.rect)

        
        # Check collision between player and enemy
        if pygame.sprite.spritecollideany(player, enemy_sprites):
               sound_crach.play()
               time.sleep(1) # wait 1 sec

               #stop the game loop
               running = False

               # Stop background music and play game over sound
               pygame.mixer.music.stop()
               sound_game_over.play()

               # Display game over screen
               screen.fill("red")
               screen.blit(image_game_over, image_game_over_rect)
               pygame.display.flip()

               time.sleep(3)

        # Check collision between player and coin
        if pygame.sprite.spritecollideany(player, coin_sprites):
               sound_coin.play() #play coin earning sound
               earned_coins += 100 #increase score
               coin.respawn_time = pygame.time.get_ticks() + random.randint(2000, 5000) #set random spawn delay
               coin.generate_rand_rect()

        
        
        # Update display and set FPS 
        pygame.display.flip()
        clock.tick(FPS)