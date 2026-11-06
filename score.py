import pygame as pg
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


class Score:
    def __init__(self, scale_factor, small_ratio=0.6):

        self.img_scorelist = self.load_digits(scale_factor)
        self.img_small_list = self.load_digits(scale_factor * small_ratio)

    def load_digits(self, scale):
        # loads 0.png to 9.png in order, so position 0 is the zero image
        return [
            pg.transform.scale_by(
                pg.image.load(
                    str(ROOT_DIR / "images" / "score" / f"{i}.png")
                ).convert_alpha(),
                scale,
            )
            for i in range(10)
        ]

    def width(self, number, small=False):
        digits = self.img_small_list if small else self.img_scorelist
        # total width of all digit images in this number
        return sum(digits[int(ch)].get_width() for ch in str(number))

    def draw_score(self, win, number, x, y, small=False):
        digits = self.img_small_list if small else self.img_scorelist
        for ch in str(number):              # 10 becomes '1', then '0'
            img = digits[int(ch)]           # picks the image from the list
            win.blit(img, (x, y))           # draws it
            x += img.get_width()            # moves right for the next digit