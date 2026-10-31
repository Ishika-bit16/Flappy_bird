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
        self.rect = self.image.get_rect(center=(280, 350))
        self.y_position = float(self.rect.y)
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 200
        self.anim_counter = 0

        self.outflap = pg.transform.scale_by(
            pg.image.load(
                str(ROOT_DIR / "images" / "outflap.png")
            ).convert_alpha(),
            scale_factor,
        )


    def update(self,dt):
        self.y_velocity += self.gravity * dt
        self.y_position += self.y_velocity
        self.rect.y = round(self.y_position)

    def flap(self, dt):
        self.y_velocity =-self.flap_speed*dt

    def playAnimation(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN or event.key == pg.K_SPACE or event.key == pg.K_UP:
                 self.image_index = 0
        else:
            self.image_index = 1    # up and down wings

        self.image = self.img_list[self.image_index]
