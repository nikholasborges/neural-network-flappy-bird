import pygame
from Util.GameConstants import Floor as Constants


class Floor:

    def __init__(self, y):
        self.img = pygame.image.load(Constants.FLOOR_SPRITE).convert_alpha()
        self.width = self.img.get_width()

        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def run(self):
        self.x1 -= Constants.VELOCITY
        self.x2 -= Constants.VELOCITY

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def render(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
