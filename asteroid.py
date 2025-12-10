from random import uniform

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_degree = uniform(20, 51)
            asteroid_1_movement = self.velocity.rotate(random_degree)
            asteroid_2_movement = self.velocity.rotate(-random_degree)
            asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
            asteroid1.velocity = asteroid_1_movement * 1.2
            asteroid2.velocity = asteroid_2_movement * 1.2
