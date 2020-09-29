from Util.GameConstants import Bird as Constants
import pygame


class Bird:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = self.y

        self.sprite_frames = 0
        self.max_sprite_frames = len(Constants.BIRD_SPRITE)
        self.img = pygame.image.load(Constants.BIRD_SPRITE[0])

        self.tilt = 0
        self.tick_count = 0
        self.velocity = 3
        self.displacement_limit = Constants.DISPLACEMENT_LIMIT

        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def jump(self):
        self.velocity = Constants.JUMP_HEIGHT
        self.tick_count = 0
        self.height = self.y

    def run(self):

        # get keys pressed

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            self.jump()

        # set bird frames per frame_rate value
        now = pygame.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.sprite_frames += 1
            if self.sprite_frames > self.max_sprite_frames - 1:
                self.sprite_frames = 0

        # Calculates the displacement value of the object
        self.tick_count += 1

        displacement = self.velocity * self.tick_count + (1.5 * (self.tick_count ** 2))

        # Debug
        # if key_pressed[pygame.K_o]:
        #     displacement = 0

        if displacement >= self.displacement_limit:
            displacement = self.displacement_limit
        elif displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        # decides if the object is falling and set falling angle
        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < Constants.MAX_ROTATION:
                self.tilt = Constants.MAX_ROTATION
        else:
            if self.tilt > - 90:
                self.tilt -= Constants.ROTATION_VELOCITY

    def render(self, window):

        # render object sprites
        self.img = pygame.image.load(Constants.BIRD_SPRITE[self.sprite_frames]).convert_alpha()

        # Rotate in the corner of the bird sprite
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)

        window.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
