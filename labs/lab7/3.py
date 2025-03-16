import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

running = True
x = 100
y = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - 20 - 25 >= 0:
        y -= 20
    if keys[pygame.K_DOWN] and y + 45 <= 600:
        y += 20
    if keys[pygame.K_LEFT] and x - 45 >= 0:
        x -= 20
    if keys[pygame.K_RIGHT] and x + 45 <= 800:
        x += 20

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)