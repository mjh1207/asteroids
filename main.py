import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updateable)
        
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        for asteroid in asteroids:
            if (player.check_for_collision(asteroid) == True):
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if bullet.check_for_collision(asteroid):
                    asteroid.split()
                    bullet.kill()
            
        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit framerate
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
