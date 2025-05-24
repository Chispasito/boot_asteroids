import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        rand = random.uniform(20.0, 50.0)
        new_rot = [self.velocity.rotate(rand), self.velocity.rotate(-rand)]
        self.spawn(new_rad, self.position, new_rot[0])
        self.spawn(new_rad, self.position, new_rot[1])
        
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity * 1.2