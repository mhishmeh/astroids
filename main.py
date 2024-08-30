import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable,drawable)

    Player_one = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT / 2,PLAYER_RADIUS)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for player in updateable:
            player.update(dt)
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60) / 1000
    
    
    
if __name__ == "__main__":

    main()