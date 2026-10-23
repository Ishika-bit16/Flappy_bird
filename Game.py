import pygame as pg
import sys

pg.init()


class Game:
    def __init__(self):
        self.width = 560
        self.height = 725

        self.win = pg.display.set_mode(
            (self.width, self.height)
        )

        self.clock = pg.time.Clock()

        # Ground movement speed
        self.move_speed = 200

        # -------------------------
        # Background
        # -------------------------

        bg = pg.image.load(
            "images/Background.png"
        ).convert_alpha()

        bg = bg.subsurface(
            (46, 40, 468, 640)
        )

        self.bg_img = pg.transform.scale(
            bg,
            (self.width, self.height)
        )

        # -------------------------
        # Ground
        # -------------------------

        self.ground()

        # -------------------------
        # Game Loop
        # -------------------------

        self.gameloop()

    def ground(self):
        base = pg.image.load(
            "images/base.png"
        ).convert_alpha()

        self.base = base

        self.base_width = self.base.get_width()
        self.base_height = self.base.get_height()

        # Ground Y position
        self.base_y = (
            self.height - self.base_height
        )

        # Single scrolling position
        self.ground_x = 0.0

    def gameloop(self):
        while True:

            # -------------------------
            # Delta Time
            # -------------------------

            dt = self.clock.tick(60) / 1000

            # -------------------------
            # Events
            # -------------------------

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # -------------------------
            # Update
            # -------------------------

            self.update(dt)

            # -------------------------
            # Render
            # -------------------------

            # Background
            self.win.blit(
                self.bg_img,
                (0, 0)
            )

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
                    round(
                        self.ground_x + self.base_width
                    ),
                    self.base_y
                )
            )

            # Display frame
            pg.display.flip()

    def update(self, dt):

        # Move ground
        self.ground_x -= (
            self.move_speed * dt
        )

        # Once one complete base has
        # moved off-screen, reset the
        # scrolling position.
        if self.ground_x <= -self.base_width:
            self.ground_x += self.base_width


game = Game()