import pygame
import random
from pygame.math import Vector2
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

LMBpressed = False
shift_pressed = False
ctrl_pressed = False
eraser_mode = False

THICKNESS = 5
ERASER_THICKNESS = 15


prevX = None
prevY = None


start_pos = None
end_pos = None



color = "red"


drawn_shapes = []

def draw_rect(x1, y1, x2, y2, color, thickness):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, thickness) 

def draw_circle(x1, y1, x2, y2, color, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)


while running:

    screen.fill("black")

    for shape in drawn_shapes:
        shape_type, *params = shape

        if shape_type == "line":
            pygame.draw.line(screen, *params)
        elif shape_type == "rect":
            draw_rect(*params)
        elif shape_type == "circle":
            draw_circle(*params)
        elif shape_type == "eraser":
            pygame.draw.line(screen, *params)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

            start_pos = event.pos
            
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                end_pos = event.pos


                if not shift_pressed and not ctrl_pressed and prevX is not None and not eraser_mode:
                    drawn_shapes.append(("line", color, (prevX, prevY), event.pos, THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]
                
                if eraser_mode and prevX is not None:
                    drawn_shapes.append(("eraser", "black", (prevX, prevY), event.pos, ERASER_THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

            if shift_pressed and start_pos and end_pos:
                drawn_shapes.append(("rect", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))

            if ctrl_pressed and start_pos and end_pos:
                drawn_shapes.append(("circle", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))

            start_pos = None
            end_pos = None


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                color = "red"
            if event.key == pygame.K_g:
                color = "green"
            if event.key == pygame.K_b:
                color = "blue"
            if event.key == pygame.K_LSHIFT:
                shift_pressed = True
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = True
            if event.key == pygame.K_e:
                eraser_mode = True
            if event.key == pygame.K_q:
                eraser_mode = False
            if event.key == pygame.K_c:
                drawn_shapes.clear()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift_pressed = False
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = False
            
    if shift_pressed and LMBpressed and start_pos and end_pos:
        draw_rect(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if ctrl_pressed and LMBpressed and start_pos and end_pos:
        draw_circle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)

    pygame.display.flip()
    clock.tick(FPS)