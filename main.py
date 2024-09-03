import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField


def main ():
    pygame.init() # initialize the gmae
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteriods, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
            
        for asteriod in asteriods:
            if asteriod.collides(player):
                print("Game over!")
                sys.exit()
        
        screen.fill((0,0,0)) #create a black screen
        
        #MUST GO AFTER THE SCREEN FILL 
        for item in drawable:
            item.draw(screen)
        

        pygame.display.flip() # refresh the screen

        dt = clock.tick(FPS)# keep this at the end of the while loop for FPS control
        dt /= 1000 # convert to seconds
    
if __name__ == "__main__":
    main()