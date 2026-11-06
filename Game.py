import pygame as pg
import sys
from pathlib import Path
from score import Score
from bird import Bird
from pipe import pipe

ROOT_DIR = Path(__file__).resolve().parent

pg.init()


class Game:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor
        self.width = 600
        self.height = 750

        self.win = pg.display.set_mode(
            (self.width, self.height)
        )

        self.clock = pg.time.Clock()
        self.is_enter_pressed = False  # started or not
        self.game_over = False
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

        self.bird = Bird(self.scale_factor)  # bird
        welcome = pg.image.load(
            str(ROOT_DIR / "images" / "welcome_page.png")
        ).convert_alpha()
        self.welcome = pg.transform.scale_by(welcome, scale_factor)

        self.pipes = []  # list for pipes
        self.pipe_counter = 71  # generate new pipes

        self.score_board = Score(self.scale_factor)
        self.score = 0  # score count
        self.high_score = self.load_high_score()  # loaded from file

        self.ground()
        self.gameloop()

    def load_high_score(self):
        try:
            return int((ROOT_DIR / "highscore.txt").read_text())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        (ROOT_DIR / "highscore.txt").write_text(str(self.high_score))

    def ground(self):
        base = pg.image.load(
            str(ROOT_DIR / "images" / "base.png")
        ).convert_alpha()  # moving base
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
                    if event.key in (pg.K_RETURN, pg.K_SPACE, pg.K_UP):
                        if self.game_over:
                            # only reset: welcome page shows again
                            self.reset_game()
                        else:
                            self.is_enter_pressed = True
                            self.bird.flap(dt)

                self.bird.playAnimation(event)

            self.update(dt)

            self.win.blit(self.bg_img, (0, 0))

            if not self.is_enter_pressed:
                self.win.blit(self.welcome, (142, 79))

            for current_pipe in self.pipes:
                current_pipe.draw(self.win)

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
                    round(self.ground_x + self.base_width), self.base_y
                )
            )

            if self.is_enter_pressed:
                self.win.blit(self.bird.image, self.bird.rect)

            # Draw the score after drawing the background and game objects.
            score_width = self.score_board.width(self.score)
            self.score_board.draw_score(
                self.win,
                self.score,
                (self.width - score_width) // 2,
                40
            )

            high_score_width = self.score_board.width(self.high_score, small=True)
            self.score_board.draw_score(
                self.win,
                self.high_score,
                self.width - high_score_width - 15,
                15,
                small=True
            )

            pg.display.flip()

    def reset_game(self):
        self.game_over = False
        self.is_enter_pressed = False
        self.bird = Bird(self.scale_factor)
        self.pipes.clear()
        self.pipe_counter = 71
        self.ground_x = 0
        self.score = 0  # high_score is NOT reset, so it is kept

    def check_collision(self):
        if self.bird.rect.bottom > self.base_y:
            self.bird.crash()
            self.game_over = True

        for current_pipe in self.pipes:
            if (
                self.bird.rect.colliderect(current_pipe.rect_top)
                or self.bird.rect.colliderect(current_pipe.rect_bottom)
            ):
                self.bird.crash()
                self.game_over = True
                break

    def update(self, dt):
        if self.is_enter_pressed and not self.game_over:
            self.ground_x -= self.move_speed * dt

            if self.ground_x <= -self.base_width:
                self.ground_x += self.base_width

            self.bird.update(dt)

            if self.pipe_counter > 70:
                self.pipes.append(pipe(self.scale_factor, self.move_speed))
                self.pipe_counter = 0
            self.pipe_counter += 1

            for current_pipe in self.pipes:
                current_pipe.update(dt)

                # the bird has gone past this pipe: add one point, once
                if (
                    not current_pipe.passed
                    and current_pipe.rect_top.right < self.bird.rect.left
                ):
                    current_pipe.passed = True
                    self.score += 1
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()

            self.pipes = [
                current_pipe
                for current_pipe in self.pipes
                if current_pipe.rect_top.right > 0
            ]
            self.check_collision()


if __name__ == "__main__":
    game = Game(scale_factor=1.5)