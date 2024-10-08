from circleshape import *
from pygame import *
from constants import *
import random
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
        else:
            angle = random.uniform(20,50)
            Vector1 = pygame.math.Vector2.rotate(self.velocity, angle)
            Vector2 = pygame.math.Vector2.rotate(self.velocity, -(angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)

            asteroid_1.velocity = Vector1 * 1.2
            asteroid_2.velocity = Vector2 * 1.2
        
