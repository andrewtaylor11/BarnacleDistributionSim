import pygame
import random
import math
import csv

# Square dimensions
square_size = 1000
circle_radius_range = (3,	100)
circle_color = (255, 0, 0)  # Red color
grid_color = (0, 255, 0)
max_iterations = 16

# Function to check collision between circles
def check_collision(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distance <= r1 + r2:
        return True
    return False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((square_size, square_size))
pygame.display.set_caption("Barnacle Distribution Simulation")

# Create a list to store the circles
circles = []

# Grid dimensions
grid_size = int(math.sqrt(square_size * square_size / 100))  # Number of points per row/column

# Generate grid points
grid_points = [(i, j) for i in range(grid_size) for j in range(grid_size)]

# Shuffle the grid points once
random.shuffle(grid_points)

# Iterate until no more circles can fit or maximum iterations reached
iteration = 0
max_radius = circle_radius_range[1]  # Initial maximum radius
while iteration < max_iterations:
    circles_placed = False

    # Iterate over grid points
    for i, j in grid_points:
        x = (i + 0.5) * (square_size / grid_size)
        y = (j + 0.5) * (square_size / grid_size)
        radius_min, radius_max = circle_radius_range

        # Randomly select a radius within the range
        radius = random.uniform(radius_min, min(radius_max, max_radius))

        # Check collision and place the circle if no collision
        collision = False
        for circle in circles:
            if check_collision(x, y, radius, circle[0], circle[1], circle[2]):
                collision = True
                break
        if not collision:
            circles.append((x, y, radius))
            circles_placed = True

    if not circles_placed:
        break

    # Shuffle the grid points again for the next iteration
    random.shuffle(grid_points)
    iteration += 1

    # Decrease the maximum radius
    max_radius = circle_radius_range[1] - (iteration / max_iterations) * (circle_radius_range[1] - circle_radius_range[0])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the square
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, square_size, square_size), 2)

    # Draw the circles
    for x, y, radius in circles:
        pygame.draw.circle(screen, circle_color, (int(x), int(y)), radius)

    # Draw the grid points
    for i, j in grid_points:
        x = (i + 0.5) * (square_size / grid_size)
        y = (j + 0.5) * (square_size / grid_size)
        pygame.draw.circle(screen, grid_color, (int(x), int(y)), 1)

    # Update the display
    pygame.display.flip()


# Export circles to a CSV file
with open('circle_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'radius'])  # Write header
    for circle in circles:
        writer.writerow(tuple(circle[:2]) + (circle[2],))  # Write circle coordinates and radius

print('complete')
# Quit the program
pygame.quit()
