import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player
import pygame as pg # type: ignore
import constants
from logger import log_state, log_event

def main():
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock = pg.time.Clock()
    dt = 0
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        log_state()

        dt = clock.tick(60) / 1000

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        for sprite in drawable:
            sprite.draw(screen)

        pg.display.flip()


if __name__ == "__main__":
    main()
