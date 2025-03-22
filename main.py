# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from AsteroidField import *
from shot import *


print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (astroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers=(shots, updateable, drawable)


    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        updateable.update(dt)
        for asteroid in astroids:
            if asteroid.collision_check(player) == True:
                raise SystemExit("Game Over!")
        for asteroid in astroids:
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.kill()
                    shot.kill()

        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    
    main()
