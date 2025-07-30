import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        
        small_vel_1 = self.velocity.rotate(random_angle)
        small_vel_2 = self.velocity.rotate(-random_angle)

        small_radius = self.radius - ASTEROID_MIN_RADIUS
        
        small_asteroid_1 = Asteroid(self.position.x, self.position.y, small_radius)
        small_asteroid_1.velocity = small_vel_1 * 1.2
        
        small_asteroid_2 = Asteroid(self.position.x, self.position.y, small_radius)
        small_asteroid_2.velocity = small_vel_2 * 1.2