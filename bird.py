import pygame as pg
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

class Bird(pg.sprite.Sprite):
    def __init__(self, scale_factor):
        super().__init__()
        self.img_list = [
            pg.transform.scale_by(
                pg.image.load(
                    str(ROOT_DIR / "images" / "upflap.png")
                ).convert_alpha(),
                scale_factor,
            ),
            pg.transform.scale_by(
                pg.image.load(
                    str(ROOT_DIR / "images" / "downflap.png")
                ).convert_alpha(),
                scale_factor,
            ),
        ]
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center=(100, 100))
