import pygame
import random
from pygame.math import Vector2
import time
import math

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

square_mode = False # drawing a square
right_triangle_mode = False # drawing a right triangle
equilateral_triangle_mode = False # drawing a equilateral triangle
rhombus_mode = False # drawing a rhombus

# Drawing settings
THICKNESS = 5
ERASER_THICKNESS = 15


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


# Function to draw a right triangle
def draw_right_triangle(right_triangle_points, color, thickness):
    pygame.draw.polygon(screen, color, right_triangle_points, thickness)

# Function to draw a equilateral triangle
def draw_equilateral_triangle(triangle_points, color, thickness):
    pygame.draw.polygon(screen, color, triangle_points, thickness)

# Function to draw a rhombus
def draw_rhombus(rhombus_points, color, thickness):
    pygame.draw.polygon(screen, color, rhombus_points, thickness)

# Function to calculate equilateral triangle's points
def get_triangle_points(center, side_length):
    #Returns the three vertex points of an equilateral triangle
    x, y = center
    height = (math.sqrt(3) / 2) * side_length  # Triangle height

    point1 = (x, y - (2/3) * height)
    point2 = (x - side_length / 2, y + (1/3) * height)
    point3 = (x + side_length / 2, y + (1/3) * height)

    return [point1, point2, point3]


def get_rhombus_points(center, width, height):
    # Returns the four vertex points of a rhombus.
    x, y = center
    return [
        (x, y - height // 2),   # Top
        (x + width // 2, y),    # Right
        (x, y + height // 2),   # Bottom
        (x - width // 2, y)     # Left
    ]


while running:
    # Fill the screen with black to refresh the drawing
    screen.fill("black")

    # Redraw all saved shapes
    for shape in drawn_shapes:
        shape_type, *params = shape

        if shape_type == "square":
            draw_rect(*params)
        elif shape_type == "right triangle":
            draw_right_triangle(*params)
        elif shape_type == "equilateral triangle":
            draw_equilateral_triangle(*params)
        elif shape_type == "rhombus":
            draw_rhombus(*params)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse button press event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            # Store start position for shapes
            start_pos = event.pos
            
        # Mouse movement event
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                end_pos = event.pos


        # Mouse button release event
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False


            #Save and drawing triangles
            if right_triangle_mode and start_pos and end_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Create a right triangle (ensuring 90-degree angle)
                right_triangle = [
                    (x1, y1),  # First point
                    (x2, y2),  # Second point
                    (x1, y2)   # Right angle point
                ]
                drawn_shapes.append(("right triangle", right_triangle, color, THICKNESS))


            #Save and drawing squares
            if square_mode and start_pos and end_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Determine square side length
                side_length = min(abs(x2 - x1), abs(y2 - y1))

                # Ensure the square remains aligned with the start position
                if x2 < x1:
                    x1 -= side_length
                if y2 < y1:
                    y1 -= side_length
                drawn_shapes.append(("square", x1, y1, x1 + side_length, y1 + side_length, color, THICKNESS))

            #Save and drawing triangles
            if equilateral_triangle_mode and start_pos and end_pos:
                side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                drawn_shapes.append(("equilateral triangle", get_triangle_points(start_pos, side_length), color, THICKNESS))

            #Save and drawing rhombuses
            if rhombus_mode and start_pos and end_pos:
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)

                drawn_shapes.append(("rhombus", get_rhombus_points(center, width, height), color, THICKNESS))

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
            if event.key == pygame.K_c: # clear the screen
                drawn_shapes.clear()
            
            #activating keys for shapes
            if event.key == pygame.K_a: 
                square_mode = True
            if event.key == pygame.K_d:
                right_triangle_mode = True
            if event.key == pygame.K_f:
                equilateral_triangle_mode = True
            if event.key == pygame.K_i:
                rhombus_mode = True

            # Deactivating keys for drawing shapes
            if event.key == pygame.K_z:
                square_mode = False
            if event.key == pygame.K_e:
                right_triangle_mode = False
            if event.key == pygame.K_h:
                equilateral_triangle_mode = False
            if event.key == pygame.K_j:
                rhombus_mode = False

            
    # Preview shapes while drawing
    # Not saving them
    if square_mode and LMBpressed and start_pos and end_pos:
        x1, y1 = start_pos
        x2, y2 = end_pos

        # Determine square side length
        side_length = min(abs(x2 - x1), abs(y2 - y1))

        # Ensure the square remains aligned with the start position
        if x2 < x1:
            x1 -= side_length
        if y2 < y1:
            y1 -= side_length
        draw_rect(x1, y1, x1+ side_length, y1 + side_length, color, THICKNESS)

    if right_triangle_mode and LMBpressed and start_pos and end_pos:
        x1, y1 = start_pos
        x2, y2 = end_pos

        # Create a right triangle (ensuring 90-degree angle)
        right_triangle = [
            (x1, y1),  # First point
            (x2, y2),  # Second point
            (x1, y2)   # Right angle point
        ]

        draw_right_triangle(right_triangle, color, THICKNESS)

    if equilateral_triangle_mode and LMBpressed and start_pos and end_pos:
        side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
        draw_equilateral_triangle(get_triangle_points(start_pos, side_length), color, THICKNESS)

    if rhombus_mode and LMBpressed and start_pos and end_pos:
        width = abs(end_pos[0] - start_pos[0])
        height = abs(end_pos[1] - start_pos[1])
        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)

        draw_rhombus(get_rhombus_points(center, width, height), color, THICKNESS)

    pygame.display.flip()
    clock.tick(FPS)