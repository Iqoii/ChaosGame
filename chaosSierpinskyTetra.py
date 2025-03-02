import pygame
import sys
import math
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 1200, 1000  # Screen dimensions
BG_COLOR = (255, 255, 255)  # White background
DOT_COLOR = (0, 0, 255)     # Blue dot color for tetrahedron edges
CHAOS_DOT_COLOR = (255, 0, 0)  # Red dot color for chaos points
TEXT_COLOR = (0, 0, 0)
DOT_RADIUS = 2  # Size of chaos points 

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Tetrahedron with 3D Chaos Game")

font = pygame.font.SysFont(None, 36)

# Vertices of a tetrahedron in 3D
vertices_3d = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
])

# Scaling factor for size
scale = 300

# Rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Chaos game variables
chaos_points = []
current_point = np.array([0.0, 0.0, 0.0])  # Start from the center of the tetrahedron

total_iterations = 0         # Total iterations counter

# 3D projection function
def project(point):
    """ Projects a 3D point onto the 2D screen. """
    x = int(point[0] * scale + WIDTH / 2)
    y = int(point[1] * scale + HEIGHT / 2)
    return (x, y)

# Rotate a 3D point using the rotation matrices
def rotate_point_3d(point, angle_x, angle_y, angle_z):
    rotation_x = np.array([
        [1, 0, 0],
        [0, math.cos(angle_x), -math.sin(angle_x)],
        [0, math.sin(angle_x), math.cos(angle_x)]
    ])

    rotation_y = np.array([
        [math.cos(angle_y), 0, math.sin(angle_y)],
        [0, 1, 0],
        [-math.sin(angle_y), 0, math.cos(angle_y)]
    ])

    rotation_z = np.array([
        [math.cos(angle_z), -math.sin(angle_z), 0],
        [math.sin(angle_z), math.cos(angle_z), 0],
        [0, 0, 1]
    ])

    rotated_point = np.dot(rotation_x, point)
    rotated_point = np.dot(rotation_y, rotated_point)
    rotated_point = np.dot(rotation_z, rotated_point)

    return rotated_point

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with background color
    screen.fill(BG_COLOR)

    # Rotate and project tetrahedron vertices
    rotated_vertices = []
    for vertex in vertices_3d:
        rotated_vertex = rotate_point_3d(vertex, angle_x, angle_y, angle_z)
        rotated_vertices.append(rotated_vertex)

    # Project the rotated vertices to 2D
    points_2d = [project(vertex) for vertex in rotated_vertices]
 
    # Draw tetrahedron edges
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3)]
    for edge in edges:
        pygame.draw.line(screen, DOT_COLOR, points_2d[edge[0]], points_2d[edge[1]], 2)

    # Chaos game: generate new chaos points in 3D

    # Choose a random vertex from the tetrahedron (non-rotated vertices)
    chosen_vertex = random.choice(vertices_3d)
    # Move halfway towards the chosen vertex
    current_point = (current_point + chosen_vertex) / 2
    # Add the new point to the chaos points list
    chaos_points.append(current_point)
    # Increment total iterations
    total_iterations += 1

    # Rotate and project chaos points
    for chaos_point in chaos_points:
        # Rotate the chaos point in 3D
        rotated_chaos_point = rotate_point_3d(chaos_point, angle_x, angle_y, angle_z)

        # Project and draw the rotated chaos point
        projected_chaos_point = project(rotated_chaos_point)
        pygame.draw.circle(screen, CHAOS_DOT_COLOR, projected_chaos_point, DOT_RADIUS)

    # Update rotation angles for the next frame
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    # Display the number of chaos iterations
    iterations_text = font.render(f"Total Chaos Iterations: {total_iterations}", True, TEXT_COLOR)
    screen.blit(iterations_text, (WIDTH - iterations_text.get_width() - 20, 20))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
