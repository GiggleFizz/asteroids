# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for entity in asteroids:
            if player.collision(entity):
                raise SystemExit("Game over!")
        for drawerables in drawable:
            drawerables.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()