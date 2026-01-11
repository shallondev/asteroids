import pygame as pg # type: ignore
import constants
from logger import log_state

def main():
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock = pg.time.Clock()
    dt = 0

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        log_state()
        screen.fill("black")
        pg.display.flip()

        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()
