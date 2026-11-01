import pygame as pg
from random import randint
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

class pipe:

    def __init__(self, scale_factor, move_speed):
        self.imgup = pg.transform.scale_by(pg.image.load(str(ROOT_DIR / "images/UpPipe.png")).convert_alpha(), scale_factor)
        self.imgdown = pg.transform.scale_by(pg.image.load(str(ROOT_DIR / "images/DownPipe.png")).convert_alpha(),scale_factor)
        self.rect_up = self.imgup.get_rect()
        self.rect_down = self.imgdown.get_rect()
        self.move_speed = move_speed

        self.pipe_dist = 80 # distance btw both pipe
        #position of both pipes
        self.rect_up.y = randint(250,520)
        self.rect_up.x = 600
        self.rect_down.y= self.rect_up.height -self.pipe_dist- self.rect_up.y
        self.rect_down.x=600

    def draw(self, win):
        win.blit(self.imgup,self.rect_up)
        win.blit(self.imgdown,self.rect_down)

    def update(self,dt):
        distance = self.move_speed * dt
        self.rect_up.x -= round(distance)
        self.rect_down.x -= round(distance)




