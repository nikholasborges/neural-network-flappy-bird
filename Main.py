import random
import pygame
import os
import neat
from Controller import GameController
from Util.GameConstants import Global as Constants
from Util.NeatConstants import NeatConstants
from Model import Bird


class Main:

    def __init__(self):

        self.neat_config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                         NeatConstants.CONFIG_PATH)

        self.population = neat.Population(self.neat_config)
        self.population.add_reporter(neat.StdOutReporter(True))
        self.population.add_reporter(neat.StatisticsReporter())

        # game configs
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        pygame.display.set_caption('Flappy Bird Neural Network')

    def start(self):
        self.population.run(self.fitness_function, 20)

    def fitness_function(self, genomes, config):
        window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        game = GameController.Game()

        networks = []
        genomes_list = []

        for genome_id, genome in genomes:
            network = neat.nn.FeedForwardNetwork.create(genome, config)
            networks.append(network)
            game.birds.append(Bird.Bird(random.randint(200, 300), 250))
            genome.fitness = 0
            genomes_list.append(genome)

        clock = pygame.time.Clock()
        fps = 30

        run = True

        # main game loop
        while run:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            game.run(networks, genomes_list)
            game.render(window, self.population.generation)

            if len(networks) == 0:
                run = False
        # debug
        stats_title = '*' * 5 + ' Best Generation Bird Stats ' + '*' * 5

        print('')
        print(stats_title)
        print(f'Best Genome Fitness: {game.sorted_genomes[0].fitness}')
        print(f'Best Bird Score: {game.best_bird.score}')
        print(f'Best Network: {game.best_network}')
        print('*' * len(stats_title))
        print('')


if __name__ == '__main__':
    main = Main()
    main.start()
