from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame as pg # type: ignore

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    