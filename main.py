import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if player.has_collided(asteroid):
                print("Game Over!")
                sys.exit(69)
            for shot in shots:
                if asteroid.has_collided(shot):
                    asteroid.kill()
                    shot.kill()
                
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        

        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()