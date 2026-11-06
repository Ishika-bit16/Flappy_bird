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
        self.gravity = 800
        self.flap_speed = 300
        self.anim_counter = 0
        self.animation_timer = 0.0

        self.outflap = pg.transform.scale_by(
            pg.image.load(
                str(ROOT_DIR / "images" / "outflap.png")
            ).convert_alpha(),
            scale_factor,
        )
        self.gravity_ON = True


    def update(self,dt):
        if self.gravity_ON:
            self.y_velocity += self.gravity * dt
            self.y_position += self.y_velocity * dt
        self.animation_timer += dt
        if self.animation_timer >= 0.1:
            self.image_index = 1 - self.image_index
            self.animation_timer = 0.0
            self.image = self.img_list[self.image_index]
        self.rect.y = round(self.y_position)

    def flap(self, dt):
        self.y_velocity = -self.flap_speed
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.animation_timer = 0.0

    def crash(self):
        self.gravity_ON = False
        self.image = self.outflap

    def playAnimation(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_RETURN, pg.K_SPACE, pg.K_UP):
                self.image_index = 0
                self.image = self.img_list[self.image_index]
