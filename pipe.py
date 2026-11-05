import pygame as pg
from random import randint
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent


class pipe:

    def __init__(self, scale_factor, move_speed):

        self.img_top = pg.transform.scale_by(
            pg.image.load(str(ROOT_DIR / "images" / "DownPipe.png")).convert_alpha(),
            scale_factor,
        )
        self.img_bottom = pg.transform.scale_by(
            pg.image.load(str(ROOT_DIR / "images" / "UpPipe.png")).convert_alpha(),
            scale_factor,
        )

        self.rect_top = self.img_top.get_rect()
        self.rect_bottom = self.img_bottom.get_rect()
        self.move_speed = move_speed

        self.pipe_dist = 170  # fixed gap between the two pipes

        # ONE random value decides where the gap starts.
        gap_top = randint(120, 350)

        # Top pipe ends at gap_top, bottom pipe starts gap_top + gap below it.
        self.rect_top.bottom = gap_top
        self.rect_bottom.top = gap_top + self.pipe_dist

        # Float x so small movements are not lost to rounding.
        self.x = 600.0
        self.rect_top.x = round(self.x)
        self.rect_bottom.x = round(self.x)

    def draw(self, win):
        win.blit(self.img_top, self.rect_top)
        win.blit(self.img_bottom, self.rect_bottom)

    def update(self, dt):
        self.x -= self.move_speed * dt
        # Both pipes always get the exact same x.
        self.rect_top.x = round(self.x)
        self.rect_bottom.x = round(self.x)