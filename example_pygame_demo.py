# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Canvas dimensions
canvas_width = 800
canvas_height = 600

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Create the canvas
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Robot Navigation")

# Robot properties
robot_radius = 20
robot_x = canvas_width // 2
robot_y = canvas_height // 2
robot_speed = 5

# Goal properties
goal_radius = 20
goal_x = canvas_width // 2
goal_y = canvas_height // 2


# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((255, 255, 255))

    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= 0.1*robot_speed
    if keys[pygame.K_RIGHT]:
        robot_x += 0.1*robot_speed
    if keys[pygame.K_UP]:
        robot_y -= 0.1*robot_speed
    if keys[pygame.K_DOWN]:
        robot_y += 0.1*robot_speed

    # Draw the goal

    pygame.draw.circle(screen, red, (goal_x, goal_y), goal_radius)

    # Draw the robot
    pygame.draw.circle(screen, blue, (robot_x, robot_y), robot_radius)

    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()
