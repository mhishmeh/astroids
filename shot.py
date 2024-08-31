from circleshape import *
from constants import *
class Shot(CircleShape):
    def __init__(self,x,y,):
        super().__init__(x,y, SHOT_RADAIUS)
        

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, SHOT_RADAIUS)

    def update(self, dt):
        self.position += self.velocity * dt