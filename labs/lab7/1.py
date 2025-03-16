import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((850, 600))
done = False

clock_image = pygame.image.load("C:/Users/kajra/OneDrive/Рабочий стол/PP2_spring_2025/labs/lab7/images/clock.png")
min_hand = pygame.image.load("C:/Users/kajra/OneDrive/Рабочий стол/PP2_spring_2025/labs/lab7/images/min_hand.png")
sec_hand = pygame.image.load("C:/Users/kajra/OneDrive/Рабочий стол/PP2_spring_2025/labs/lab7/images/sec_hand.png")

clock_image = pygame.transform.scale(clock_image, (850, 600))

clock = pygame.time.Clock()

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = (x, y))

    return rotated_image, new_rect

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        current_time = datetime.datetime.now()
        seconds = current_time.second
        minutes = current_time.minute

        second_angle = -seconds * 6 + 60
        minute_angle = -minutes * 6 - seconds * 0.1 - 48

        rotated_minute, minute_rect = rot_center(min_hand, minute_angle, 425, 300)
        rotated_second, second_rect = rot_center(sec_hand, second_angle, 425, 300)

        screen.blit(clock_image, (0, 0))
        screen.blit(rotated_minute, minute_rect)
        screen.blit(rotated_second, second_rect )
        

        pygame.display.flip()
        clock.tick(30)