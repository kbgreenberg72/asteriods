import pygame
from constants import *
from player import Player


def main ():
    pygame.init() # initialize the gmae
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 # delta time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0)) #create a black screen
        player.draw(screen)
        pygame.display.flip() # refresh the screen

        dt = clock.tick(FPS)# keep this at the end of the while loop for FPS control
        dt /= 1000 # convert to seconds
    
if __name__ == "__main__":
    main()