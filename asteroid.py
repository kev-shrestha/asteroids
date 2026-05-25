from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):    
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else: 
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            new_asteroid_one_vector = self.velocity.rotate(new_angle)
            new_asteroid_two_vector = self.velocity.rotate(-new_angle)

            new_smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_smaller_asteroid_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_smaller_asteroid_radius)

            asteroid_one.velocity = pygame.Vector2(new_asteroid_one_vector) * 1.2
            asteroid_two.velocity = pygame.Vector2(new_asteroid_two_vector) * 1.2
