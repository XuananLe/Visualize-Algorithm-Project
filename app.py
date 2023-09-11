import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NODE_RADIUS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Animation")

nodes = {
    'A': [100, 100],
    'B': [300, 200],
    'C': [500, 300],
    'D': [400, 100],
    'E': [600, 200]
}

edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('A', 'D'),
    ('D', 'E')
]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Animate nodes (random movement)
    for node, (x, y) in nodes.items():
        dx, dy = random.randint(-5, 5), random.randint(-5, 5)
        nodes[node][0] += dx
        nodes[node][1] += dy
        pygame.draw.circle(screen, BLACK, (x, y), NODE_RADIUS)
        font = pygame.font.Font(None, 36)
        text = font.render(node, True, BLACK)
        screen.blit(text, (x - NODE_RADIUS // 2, y - NODE_RADIUS // 2))

    # Draw edges
    for edge in edges:
        start_node = nodes[edge[0]]
        end_node = nodes[edge[1]]
        pygame.draw.line(screen, BLACK, start_node, end_node, 2)

    pygame.display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS

# Quit Pygame
pygame.quit()
sys.exit()
