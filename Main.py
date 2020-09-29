import pygame
import os
from Controller import GameController
from Util.GameConstants import Global as Constants


def start():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Neural Network')
    game = GameController.Game()

    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.run()
        game.render(window)

    pygame.quit()


if __name__ == '__main__':
    start()
