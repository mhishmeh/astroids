import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    Player_one = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT / 2,PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        Player_one.draw(screen)
        Player_one.update(dt)
        pygame.display.flip()

        dt = fps.tick(60) / 1000
    
    
    
if __name__ == "__main__":

    main()