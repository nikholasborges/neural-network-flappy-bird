import pygame
import os
import neat
from Controller import GameController
from Util.GameConstants import Global as Constants
from Util.NeatConstants import NeatConstants
from Model import Bird


def start():
    # neat config
    neat_config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                     NeatConstants.CONFIG_PATH)

    population = neat.Population(neat_config)
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    # game configs
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    pygame.display.set_caption('Flappy Bird Neural Network')

    winner = population.run(fitness_function, 20)


def fitness_function(genomes, config):
    window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    game = GameController.Game()

    networks = []
    genomes_list = []

    for genome_id, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        game.birds.append(Bird.Bird(250, 250))
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
        game.render(window)

        if len(networks) == 0:
            run = False

    print('')
    print(f'Best Genome Fitness: {game.sorted_genomes[0].fitness}')
    print(f'Best Bird Score: {game.best_bird.score}')
    print(f'Best Network: {game.best_network}')
    print('')


if __name__ == '__main__':
    start()
