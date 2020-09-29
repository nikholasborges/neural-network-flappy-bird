import pygame
from Controller import GameController
from Util.GameConstants import Global as Constants


def start():
    pygame.init()
    window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption('Flappy Bird Neural Network')
    clock = pygame.time.Clock()  # For syncing the FPS
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
