from circleshape import *
class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y, radius)
        self.SHOT_RADIUS = 5

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS,width=1)

    def update(self, dt):
        pass