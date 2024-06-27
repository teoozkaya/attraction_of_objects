import pygame
import random
import numpy as np

class Particle:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.vel = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=float)
        self.acc = np.array([0, 0], dtype=float)

    def attracted(self, target):
        force = target - self.position
        distance = np.linalg.norm(force)
        distance = np.clip(distance, 5, 25)
        force.scale_to_length(5 / distance)
        self.acc += force

    def update(self):
        self.vel += self.acc
        self.position += self.vel
        self.acc *= 0

    def show(self, window):
        pygame.draw.circle(window, (255, 255, 255), self.position.astype(int), 2)



