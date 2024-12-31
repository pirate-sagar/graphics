import pygame
import math


# DDA Line Drawing Function
def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps
    steps = max(abs(dx), abs(dy))

    # Calculate the increment for each step
    xi = dx / steps
    yi = dy / steps

    # Starting point
    xn = x1
    yn = y1

    # Draw the line
    for _ in range(int(steps) + 1):
        pygame.draw.circle(screen, (255, 255, 255), (round(xn), round(yn)), 1)  # Draw pixel
        xn += xi
        yn += yi


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA Line Drawing")

# Set up the clock for managing frame rate
clock = pygame.time.Clock()

# Input coordinates
x1, y1 = map(int, input("Enter x1 and y1: ").split())
x2, y2 = map(int, input("Enter x2 and y2: ").split())

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Draw the line using DDA
    dda_line(x1, y1, x2, y2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
