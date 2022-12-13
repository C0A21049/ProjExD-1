import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    bg_rct.center = 800, 450
    scrn_sfc.blit(bg_sfc, bg_rct)
    pg.display.update()

    clock = pg.time.Clock()
    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

