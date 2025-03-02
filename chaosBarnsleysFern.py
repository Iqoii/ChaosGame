import pygame
import sys, random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800  # Screen dimensions
BG_COLOR = (255, 255, 255)  # White background
DOT_COLOR = (0, 0, 255)     # Blue dot color
DOT_RADIUS = 1              # Dot radius
TEXT_COLOR = (0, 0, 0)      # Text color

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos Game - Barnsley Fern")
font = pygame.font.SysFont(None, 36)

# Scaling factors for visualization
scale_x, scale_y = 80, 80  # Scale factor for better visibility
offset_x, offset_y = WIDTH // 2, HEIGHT // 10

# Initial point
x, y = 0, 0
iterations = 0
stop = False
dots = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                stop = True
            if event.key == pygame.K_1:
                stop = False
    
    iterations += 1
    
    if not stop:
        r = random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        
        # Convert to screen coordinates
        screen_x = int(scale_x * x + offset_x)
        screen_y = int(HEIGHT - (scale_y * y + offset_y))
        dots.append((screen_x, screen_y))
    
    # Fill the screen with background color
    screen.fill(BG_COLOR)
    
    # Draw all dots
    for coords in dots:
        pygame.draw.circle(screen, DOT_COLOR, coords, DOT_RADIUS)
    
    # Display iteration count
    text_surface = font.render(f"Iterations: {iterations}", True, TEXT_COLOR)
    screen.blit(text_surface, (10, 10))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
