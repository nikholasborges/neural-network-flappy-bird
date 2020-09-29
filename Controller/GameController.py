import pygame
from Model import Bird, Floor, Pipe
from Util.GameConstants import Global as Constants


class Game:
    def __init__(self):
        self.player = Bird.Bird(250, 250)

    def run(self):
        self.player.run()

    def render(self, win):
        win.blit(pygame.image.load(Constants.BACKGROUND_SPRITE).convert(), (0, 0))
        self.player.render(win)

        pygame.display.update()
