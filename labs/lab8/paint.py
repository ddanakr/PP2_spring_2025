import pygame
import random
from pygame.math import Vector2
import time

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

LMBpressed = False  # Left mouse button pressed
shift_pressed = False  # Shift key pressed
ctrl_pressed = False  # Control key pressed
eraser_mode = False  # Eraser mode active

# Drawing settings
THICKNESS = 5
ERASER_THICKNESS = 15

# Previous mouse position for drawing lines
prevX = None
prevY = None

# Start and end positions for drawing shapes
start_pos = None
end_pos = None


color = "red" #default drawing color

# List to store drawn shapes
drawn_shapes = []

# Function to draw a rectangle
def draw_rect(x1, y1, x2, y2, color, thickness):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, thickness) 

# Function to draw a circle
def draw_circle(x1, y1, x2, y2, color, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)


while running:
    # Fill the screen with black to refresh the drawing
    screen.fill("black")

    # Redraw all saved shapes
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

        # Mouse button press event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            # Store start position for shapes
            prevX = event.pos[0]
            prevY = event.pos[1]
            start_pos = event.pos
            
        # Mouse movement event
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                end_pos = event.pos

                # Drawing freehand lines
                if not shift_pressed and not ctrl_pressed and prevX is not None and not eraser_mode:
                    drawn_shapes.append(("line", color, (prevX, prevY), event.pos, THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]
               # Eraser mode 
                if eraser_mode and prevX is not None:
                    drawn_shapes.append(("eraser", "black", (prevX, prevY), event.pos, ERASER_THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]

        # Mouse button release event
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

            #Save and drawing rectangles when Shift is pressed
            if shift_pressed and start_pos and end_pos:
                drawn_shapes.append(("rect", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
            #Save and drawing circles when Ctrl is pressed
            if ctrl_pressed and start_pos and end_pos:
                drawn_shapes.append(("circle", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))

            start_pos = None
            end_pos = None


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # Increase thickness
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Deccrease thickness, can't be less than 1
            #changing the color
            if event.key == pygame.K_r:
                color = "red"
            if event.key == pygame.K_g:
                color = "green"
            if event.key == pygame.K_b:
                color = "blue"
            if event.key == pygame.K_LSHIFT: # rectangle drawing mode
                shift_pressed = True
            if event.key == pygame.K_LCTRL: # circle drawing mode
                ctrl_pressed = True
            if event.key == pygame.K_e: # eraser mode
                eraser_mode = True
            if event.key == pygame.K_q: # disable eraser mode
                eraser_mode = False
            if event.key == pygame.K_c: # clear the screen
                drawn_shapes.clear()
        
        # Key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift_pressed = False
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = False
            
    # Preview shapes while drawing
    # Not saving them
    if shift_pressed and LMBpressed and start_pos and end_pos:
        draw_rect(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if ctrl_pressed and LMBpressed and start_pos and end_pos:
        draw_circle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)

    pygame.display.flip()
    clock.tick(FPS)