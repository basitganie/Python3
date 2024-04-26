import pygame
import sys
from pygame.locals import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 1600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Cube')

# Define vertices of the cube
vertices = [
    (-250, -250, -250),
    (250, -250, -250),
    (250, 250, -250),
    (-250, 250, -250),
    (-250, -250, 250),
    (250, -250, 250),
    (250, 250, 250),
    (-250, 250, 250)
]

# Define edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define a rotation function
def rotate(vertices, angle):
    new_vertices = []
    axis = pygame.math.Vector3(1, 1, 1)  # Rotate around the y-axis
    for vertex in vertices:
        vertex_vector = pygame.math.Vector3(vertex)
        rotated_vertex = vertex_vector.rotate(angle, axis)
        new_vertices.append(rotated_vertex)
    return new_vertices
    
# Main loop
angle = 45
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    rotated_vertices = rotate(vertices, angle)
    
    for edge in edges:
        start = rotated_vertices[edge[0]]
        end = rotated_vertices[edge[1]]
        pygame.draw.line(screen, BLUE, (start[0] + WIDTH // 2, start[1] + HEIGHT // 2), (end[0] + WIDTH // 2, end[1] + HEIGHT // 2), 2)

    angle += 0.1;
    pygame.display.flip()
    clock.tick(60)
    
    