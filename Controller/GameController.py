import pygame
from Model import Bird, Floor, Pipe
from Util.GameConstants import Global as GlobalConstants
from Util.GameConstants import Pipe as PipeConstants
from Util.GameConstants import Floor as FloorConstants
from Util.GameConstants import Bird as BirdConstants


class Game:
    def __init__(self):
        self.player = Bird.Bird(BirdConstants.DEFAULT_DRAW_X_AXIS, BirdConstants.DEFAULT_DRAW_Y_AXIS)
        self.pipes = [Pipe.Pipe(PipeConstants.DRAW_SPEED)]
        self.floor = Floor.Floor(FloorConstants.DEFAULT_HEIGHT)
        self.score = 0

    def run(self):
        self.player.run()
        self.floor.run()

        remove_pipes = []
        add_pipe = False

        for pipe in self.pipes:
            if pipe.collide(self.player):
                pass

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

            if not pipe.passed and pipe.x < self.player.x:
                pipe.passed = True
                add_pipe = True

            pipe.run()

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe.Pipe(PipeConstants.DRAW_SPEED))

        for pipe in remove_pipes:
            self.pipes.remove(pipe)

        if self.player.y + self.player.img.get_height() > self.floor.y:
            pass

    def render(self, win):
        win.blit(pygame.image.load(GlobalConstants.BACKGROUND_SPRITE).convert(), (0, 0))

        self.player.render(win)

        for pipe in self.pipes:
            pipe.render(win)

        self.floor.render(win)

        pygame.display.update()
