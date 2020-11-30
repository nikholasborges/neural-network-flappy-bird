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

        self.font = pygame.font.Font(GlobalConstants.FONT, 26)

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

                # check collisions and giving fitness penalty for failed birds
                if pipe.collide(bird):
                    bird.pipe_collided = True
                    genomes_list[self.birds.index(bird)].fitness -= 5

                if bird.y + bird.default_sprite.get_height() > self.floor.y or bird.y < 0:
                    bird.floor_collided = True
                    genomes_list[self.birds.index(bird)].fitness -= 10

                # check actual bird score and giving fitness score for passing pipes
                if not pipe.passed and pipe.x + pipe.PIPE_TOP.get_width() < bird.x:
                    genomes_list[self.birds.index(bird)].fitness += 5
                    bird.score += 1
                    pipe.passed = True
                    add_pipe = True

                # remove failed birds
                if bird.pipe_collided or bird.floor_collided:
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

    def render(self, win, generation):
        win.blit(self.background_sprite, (0, 0))

        for pipe in self.pipes:
            pipe.render(win)

        for bird in self.birds:
            bird.render(win)

        self.floor.render(win)

        generation_count = self.font.render("Generation: " + str(generation), True, (255, 255, 255))
        genomes_count = self.font.render("Genomes: " + str(len(self.sorted_genomes)), True, (255, 255, 255))
        best_bird_points = self.font.render("Best Genome Points: " + str(self.best_bird.score), True, (255, 255, 255))

        win.blit(generation_count, (15, 15))
        win.blit(genomes_count, (15, 55))
        win.blit(best_bird_points, (GlobalConstants.WIDTH - best_bird_points.get_width() - 15, 15))

        pygame.display.update()
