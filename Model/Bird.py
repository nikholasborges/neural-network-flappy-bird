from Util.GameConstants import Bird as BirdConstants
from Util.GameConstants import Pipe as PipeConstants
import pygame
import random


class Bird:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = self.y

        self.sprite_frames = 0
        self.bird_sprite_list = BirdConstants.BIRD_SPRITE_DICT[
            str(random.randint(1, len(BirdConstants.BIRD_SPRITE_DICT)))]
        self.default_sprite = pygame.image.load(self.bird_sprite_list[0]).convert_alpha()
        self.bird_sprite = [pygame.image.load(self.bird_sprite_list[0]).convert_alpha(),
                            pygame.image.load(self.bird_sprite_list[1]).convert_alpha(),
                            pygame.image.load(self.bird_sprite_list[2]).convert_alpha(),
                            pygame.image.load(self.bird_sprite_list[3]).convert_alpha()]

        self.max_sprite_frames = len(self.bird_sprite_list)

        self.tilt = 0
        self.tick_count = 0
        self.velocity = 3
        self.displacement = 0
        self.displacement_limit = BirdConstants.DISPLACEMENT_LIMIT

        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30

        self.score = 0

        self.pipe_collided = False
        self.floor_collided = False

    def jump(self):
        if not self.pipe_collided and not self.floor_collided:
            self.velocity = BirdConstants.JUMP_HEIGHT
            self.tick_count = 0
            self.height = self.y

    def run(self):
        # set bird frames per frame_rate value
        now = pygame.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.sprite_frames += 1
            if self.sprite_frames > self.max_sprite_frames - 1:
                self.sprite_frames = 0

        # Calculates the displacement value of the object
        self.tick_count += 1
        self.displacement = self.velocity * self.tick_count + (1.5 * (self.tick_count ** 2))

        if self.displacement >= self.displacement_limit:
            self.displacement = self.displacement_limit
        elif self.displacement < 0:
            self.displacement -= 2

        # setting bird to stop moving if pipe collided
        if self.pipe_collided or self.floor_collided:
            self.x -= PipeConstants.VELOCITY
            self.sprite_frames = 0

        # setting bird do fall if not floor collided
        if not self.floor_collided:
            self.y = self.y + self.displacement

        # decides if the object is falling and set falling angle
        if self.displacement < 0 or self.y < self.height + 50:
            if self.tilt < BirdConstants.MAX_ROTATION:
                self.tilt = BirdConstants.MAX_ROTATION
        else:
            if self.tilt > - 90:
                self.tilt -= BirdConstants.ROTATION_VELOCITY

    def render(self, window):

        # render object sprites
        self.default_sprite = self.bird_sprite[self.sprite_frames]

        # Rotate in the corner of the bird sprite
        rotated_img = pygame.transform.rotate(self.default_sprite, self.tilt)
        new_rect = rotated_img.get_rect(center=self.default_sprite.get_rect(topleft=(self.x, self.y)).center)

        window.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.default_sprite)
