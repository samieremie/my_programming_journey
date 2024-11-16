# This file contains the help functions needed for bouncing ball
import math
import pygame
import numpy as np

# Colors used
BLACK = (0, 0, 0)

# Function that detects if the ball will fall through the arc.
def is_ball_in_arc(ball_pos, center, start_angle, end_angle):
    dx = ball_pos[0] - center[0]
    dy = ball_pos[1] - center[1]
    start_angle = start_angle % (2 * math.pi)
    end_angle = end_angle % (2 * math.pi)
    ball_angle = math.atan2(dy, dx)
    if start_angle > end_angle:
        end_angle += 2 * math.pi
    if (start_angle <= ball_angle <= end_angle or
        start_angle <= ball_angle + 2 * math.pi <= end_angle):
        return True
    else:
        return False
    
# Function that draws an arc
def draw_arc(window, center, radius, start_angle, end_angle):
    p1 = center + (radius + 100) * np.array([math.cos(start_angle), math.sin(start_angle)])
    p2 = center + (radius + 100) * np.array([math.cos(end_angle), math.sin(end_angle)])
    pygame.draw.polygon(window, BLACK, [center, p1, p2])