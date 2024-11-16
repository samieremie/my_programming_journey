# A simple simulator of bouncing balls. Satisfying to watch:)
import pygame
import numpy as np
import math
import random
from help_functions import is_ball_in_arc, draw_arc
from ball import Ball

pygame.init()

# Set width and heigth of the screen.
WIDTH = 800
HEIGHT = 600

# Create a window to draw on
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Change the title and icon of the GUI
pygame.display.set_caption("The ball simulator")
try:
    icon = pygame.image.load(r"assets\beach_ball.png")
    pygame.display.set_icon(icon)
except FileNotFoundError:
    print("Make sure the current working directory is the folder bouncing_balls")

# Create a clock
clock = pygame.time.Clock()

# The RGB for colors used in the program
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)

# Create a circle
# Make the circle center a vector. Use float for calculations.
CIRCLE_CENTER = np.array([WIDTH/2, HEIGHT/2], dtype=np.float64)
CIRCLE_RADIUS = 150

initial_ball = Ball(np.array([WIDTH/2, HEIGHT/2 - 120], dtype=np.float64), 
                    np.array([0, 0], dtype=np.float64))

# List that holds all the balls in it.
balls = [initial_ball]

# Create fake gravity
GRAVITY = 0.2 # Change the gravity 

# Create an arc (with a spinning speed)
spinning_speed = 0.01 # Use negative value for reverse spinning
arc_degree = 60 # Change the length of the arc
start_angle = math.radians((-arc_degree)/2)
end_angle = math.radians(arc_degree/2)
    
# Flag for the game loop
running = True

while running:
    for event in pygame.event.get():
        # The exit condition of the game loop.
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        # Remove the ball from the list, if it is not on the screen anymore
        if not ball.is_in and ((ball.pos[0] < 0 or ball.pos[0] > WIDTH) or
                               (ball.pos[1] < 0 or ball.pos[1] > HEIGHT)):
            balls.remove(ball)
            # Add two new balls for each ball that falls off the screen
            ball1 = Ball(np.array([WIDTH/2, HEIGHT/2 - 120], dtype=np.float64),
                         np.array([random.uniform(-4, 4), random.uniform(-1, 1)]))
            balls.append(ball1)
            ball2 = Ball(np.array([WIDTH/2, HEIGHT/2 - 120], dtype=np.float64),
                         np.array([random.uniform(-4, 4), random.uniform(-1, 1)]))
            balls.append(ball2)
            
    # Update the begin and end of the arc
    # This creates the illusion of spinning
    start_angle += spinning_speed
    end_angle += spinning_speed

    # Compute the new pos for each ball
    for ball in balls:
        # Update the speed of the ball each iteration to simulate Gravity
        ball.speed[1] += GRAVITY
        
        # Update the ball pos
        ball.pos += ball.speed

        # The math that will make the ball bounce
        # The distance of the ball to the center of the circle
        dist = np.linalg.norm(ball.pos - CIRCLE_CENTER)

        # Check if the ball is outside the circle
        if dist + ball.radius > CIRCLE_RADIUS:
            if is_ball_in_arc(ball.pos, CIRCLE_CENTER, start_angle, end_angle):
                ball.is_in = False
            if ball.is_in:
                # Calculate the vector d and the unit vector d
                d = ball.pos - CIRCLE_CENTER
                d_unit = d/ np.linalg.norm(d)
                # When the ball_pos is outside, set the pos on the circle.
                ball.pos = CIRCLE_CENTER + (CIRCLE_RADIUS - ball.radius - 3) * d_unit
                # Calculate the vector t
                t = np.array([-d[1], d[0]], dtype=np.float64)
                proj_v_t = (np.dot(ball.speed, t) / np.dot(t, t)) * t
                # Calculate the new ball speed and direction
                ball.speed = 2 * proj_v_t - ball.speed

                # Calculate the tangential force
                # This force acts on the direction
                ball.speed += t * spinning_speed

    # Draw everything
    window.fill(BLACK)
    # The big circle
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 4)
    # The arc we take out of the circle
    draw_arc(window, CIRCLE_CENTER, CIRCLE_RADIUS, start_angle, end_angle)
    # Draw each ball
    for ball in balls:
        pygame.draw.circle(window, ball.color, ball.pos, ball.radius)
    pygame.display.flip()
    clock.tick(60) # The frame rate

pygame.quit()