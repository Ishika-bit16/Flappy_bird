import pygame as pg
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


class Score:
    def __init__(self, scale_factor):
        # loads 0.png to 9.png in order, so position 0 is the zero image
        self.img_scorelist = [
            pg.transform.scale_by(
                pg.image.load(
                    str(ROOT_DIR / "images" / "score" / f"{i}.png")
                ).convert_alpha(),
                scale_factor,
            )
            for i in range(10)
        ]

    def width(self, number):
        # total width of all digit images in this number
        return sum(self.img_scorelist[int(ch)].get_width() for ch in str(number))

    def draw_score(self, win, number, x, y):
        for ch in str(number):                   # 10 becomes '1', then '0'
            img = self.img_scorelist[int(ch)]    # picks the image from the list
            win.blit(img, (x, y))                # draws it
            x += img.get_width()                 # moves right for the next digit