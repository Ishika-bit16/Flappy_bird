import pygame as pg
import sys
from pathlib import Path

from bird import Bird


ROOT_DIR = Path(__file__).resolve().parent

pg.init()


class Game:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor
        self.width = 560
        self.height = 725

        self.win = pg.display.set_mode(
            (self.width, self.height)
        )

        self.clock = pg.time.Clock()
        self.is_enter_pressed = False  # started or not
        self.is_paused = False
        self.move_speed = 200

        bg = pg.image.load(
            str(ROOT_DIR / "images" / "Background.png")
        ).convert_alpha()

        bg = bg.subsurface((46, 40, 468, 640))

        self.bg_img = pg.transform.scale(
            bg,
            (self.width, self.height)
        )
        self.win.fill((79, 190, 201))  # sky/background color
        self.win.blit(self.bg_img, (0, 0))
        self.bird = Bird(self.scale_factor)  #bird
        welcome = pg.image.load(
            str(ROOT_DIR / "images" / "welcome_page.png")
        ).convert_alpha()
        self.welcome = pg.transform.scale_by(welcome, scale_factor)


        self.ground()
        self.gameloop()

    def ground(self):
        base = pg.image.load(
            str(ROOT_DIR / "images" / "base.png")
        ).convert_alpha()        #moving base
        base = pg.transform.scale(
            base,
            (self.width, base.get_height())
        )

        self.base = base

        self.base_width = self.base.get_width()
        self.base_height = self.base.get_height()

        # Ground Y position
        self.base_y = (
            self.height - self.base_height
        )


        self.ground_x = 0

    def gameloop(self):
        while True:


            dt = self.clock.tick(60) / 1000



            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                     if (
                         not self.is_paused
                         and event.key in (pg.K_RETURN, pg.K_SPACE, pg.K_UP)
                     ):
                          self.is_enter_pressed = True
                          self.bird.flap(dt)

                self.bird.playAnimation(event)

            if not self.is_paused:
                self.update(dt)

            self.win.blit(self.bg_img, (0, 0))

            if not self.is_enter_pressed:
                self.win.blit(self.welcome, (142, 79))

            # Ground - Base 1
            self.win.blit(
                self.base,
                (
                    round(self.ground_x),
                    self.base_y
                )
            )

            # Ground - Base 2
            self.win.blit(
                self.base,
                (
                    round(self.ground_x + self.base_width ),self.base_y
                )
            )
            if self.is_enter_pressed and self.bird.rect.bottom >= self.base_y:
                self.bird.rect.bottom = self.base_y
                self.is_paused = True

            if self.is_paused:
                self.win.blit(self.bird.outflap, self.bird.rect)
            elif self.is_enter_pressed:
                self.win.blit(self.bird.image, self.bird.rect)
            pg.display.flip()

    def update(self, dt):
        if self.is_enter_pressed:
            self.ground_x -= self.move_speed * dt

            if self.ground_x <= -self.base_width:
                self.ground_x += self.base_width

            self.bird.update(dt)

if __name__ == "__main__":
    game = Game(scale_factor=1.5)