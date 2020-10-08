import pygame
from Model import Floor, Pipe
from Util.GameConstants import Global as GlobalConstants
from Util.GameConstants import Pipe as PipeConstants
from Util.GameConstants import Floor as FloorConstants


class Game:
    def __init__(self):
        self.pipes = [Pipe.Pipe(PipeConstants.DRAW_SPEED)]
        self.floor = Floor.Floor(FloorConstants.DEFAULT_HEIGHT)
        self.background_sprite = pygame.image.load(
            GlobalConstants.BACKGROUND_SPRITE).convert_alpha()

        self.birds = []

        self.sorted_genomes = []
        self.best_network = None
        self.best_bird = None

    def run(self, networks, genomes_list):

        self.floor.run()

        remove_pipes = []
        add_pipe = False

        self.sorted_genomes = sorted(genomes_list, key=lambda x: x.fitness, reverse=True)
        self.best_network = networks[genomes_list.index(self.sorted_genomes[0])]
        self.best_bird = self.birds[genomes_list.index(self.sorted_genomes[0])]

        for pipe in self.pipes:
            for bird in self.birds:

                # check collisions
                if pipe.collide(bird):
                    bird.pipe_collided = True

                if bird.y + bird.default_sprite.get_height() > self.floor.y or bird.y < 0:
                    bird.floor_collided = True

                # check actual bird score
                if not pipe.passed and pipe.x + pipe.PIPE_TOP.get_width() < bird.x:
                    genomes_list[self.birds.index(bird)].fitness += 5
                    bird.score += 1
                    pipe.passed = True
                    add_pipe = True

                # remove failed birds
                if bird.pipe_collided or bird.floor_collided:
                    genomes_list[self.birds.index(bird)].fitness -= 5
                    networks.pop(self.birds.index(bird))
                    genomes_list.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))
                else:
                    # add current bird fitness score every frame alive
                    genomes_list[self.birds.index(bird)].fitness += 0.1

                    # decide if the bird must jump or not
                    nearest_pipe_index = 0
                    if len(self.pipes) > 0:
                        if len(self.pipes) > 1 and bird.x > self.pipes[0].PIPE_TOP.get_width():
                            nearest_pipe_index = 1

                    nearest_top_pipe_distance = abs(bird.y - self.pipes[nearest_pipe_index].top)
                    nearest_bottom_pipe_distance = abs(bird.y - self.pipes[nearest_pipe_index].bottom)

                    output = networks[self.birds.index(bird)].activate([bird.y,
                                                                        nearest_top_pipe_distance,
                                                                        bird.y,
                                                                        nearest_bottom_pipe_distance])

                    if output[0] > 0.5:
                        bird.jump()

                bird.run()

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

            pipe.run()

        if add_pipe:
            self.pipes.append(Pipe.Pipe(PipeConstants.DRAW_SPEED))

        for pipe in remove_pipes:
            self.pipes.remove(pipe)

        # key_pressed = pygame.key.get_pressed()
        # if key_pressed[pygame.K_SPACE]:
        #     self.bird.jump()

    def render(self, win):
        win.blit(self.background_sprite, (0, 0))

        for pipe in self.pipes:
            pipe.render(win)

        for bird in self.birds:
            bird.render(win)

        self.floor.render(win)

        pygame.display.update()
