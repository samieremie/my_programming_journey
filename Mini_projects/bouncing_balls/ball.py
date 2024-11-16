import numpy as np
import random

# Class that generates the balls
class Ball:
    """A class that generates balls"""
    def __init__(self, position, speed):
        self.pos = np.array(position, dtype=np.float64)
        self.speed = np.array(speed, dtype=np.float64)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.is_in = True
        self.radius = 5