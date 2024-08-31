import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (updateable,drawable,asteroids)
    AsteroidField.containers = (updateable)
    AF = AsteroidField()

    Player.containers = (updateable,drawable)
    Player_one = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT / 2,PLAYER_RADIUS)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for sprite in updateable:
            sprite.update(dt)
            for obj in asteroids:
                if obj.Check_Collision(Player_one):
                    sys.exit("GAME OVER!")
        screen.fill(color="black")

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60) / 1000
    
    
    
if __name__ == "__main__":

    main()