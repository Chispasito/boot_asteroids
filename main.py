#!/usr/bin/python3
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def interpolate(x1: float, y1: float, x2: float, y2: float, x: float):
    return ((y2-y1) * x + x2 * y1 - x1 * y2) / (x2 - x1)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.Surface.fill(screen, (0,0,0))
        dt = py_clock.tick(60) / 1000
        
        for sketch in drawable:
            sketch.draw(screen)

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.check_collision(shot):
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()

        pygame.display.flip()
        

if __name__ == "__main__":
    main()