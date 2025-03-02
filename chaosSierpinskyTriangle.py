import pygame
import sys, random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 1200, 1000  # Screen dimensions
BG_COLOR = (255, 255, 255)  # White background
DOT_COLOR = (0, 0, 255)     # Blue dot color
DOT_RADIUS = 1              # Dot radius
TEXT_COLOR = (0, 0, 0)           # Dot radius

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw a Dot")

font = pygame.font.SysFont(None, 36)

# Coordinates where the dot will be placed

ix = random.randint(0, WIDTH)
iy = random.randint(0, HEIGHT)
dot_position = (ix, iy)  # Example coordinates (x, y)

iterations = 0
stop = False
dots = [(ix, iy)]

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

    # Fill the screen with background color
    screen.fill(BG_COLOR)

    # Draw the dot at the specified coordinates
    if stop != True:

        x = random.randint(1, 3)
        match x:
            case 1:
                dot_position = ((dot_position[0] + 600) / 2, (dot_position[1] + 50) / 2)
            case 2:
                dot_position = ((dot_position[0] + 1150) / 2, (dot_position[1] + 950) / 2)
            case 3:
                dot_position = ((dot_position[0] + 50) / 2, (dot_position[1] + 950) / 2)

        dots.append(dot_position)

        pygame.draw.circle(screen, (0, 0, 0), (600, 50), 3)

        pygame.draw.circle(screen, (0, 0, 0), (1150, 950), 3)

        pygame.draw.circle(screen, (0, 0, 0), (50, 950), 3)
        

        for coords in dots:
            pygame.draw.circle(screen, DOT_COLOR, coords, DOT_RADIUS)


        text_surface = font.render(f"Iterations: {iterations}", True, TEXT_COLOR)

        # Blit (draw) the text on the screen at the top-right corner
        screen.blit(text_surface, (WIDTH - text_surface.get_width() - 10, 10))  # 10 pixels padding from the right and top

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()