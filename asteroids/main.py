import pygame as pg # type: ignore
import constants
from logger import log_state

def main():
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        log_state()
        screen.fill("black")
        pg.display.flip()
    
    # print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
