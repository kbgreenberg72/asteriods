import pygame
from constants import *

def main ():
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init() # initialize the gmae
    
    clock = pygame.time.Clock()
    dt = 0 # delta time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0)) #create a black screen
        pygame.display.flip() # refresh the screen
        
        
        
        dt = clock.tick(FPS)# keep this at the end of the while loop for FPS control
        dt /= 1000 # convert to seconds
    
if __name__ == "__main__":
    main()