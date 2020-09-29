import os
import pygame


class Global:
    WIDTH = 600
    HEIGHT = 1000
    BACKGROUND_SPRITE = os.path.join('.\\Resources\\img', 'background.png')


class Bird:
    BIRD_SPRITE = [os.path.join('.\\Resources\\img', 'bird-0.png'),
                   os.path.join('.\\Resources\\img', 'bird-1.png'),
                   os.path.join('.\\Resources\\img', 'bird-2.png'),
                   os.path.join('.\\Resources\\img', 'bird-3.png')]

    MAX_ROTATION = 20
    ROTATION_VELOCITY = 20


class Pipe:
    PIPE_SPRITE = None


class Floor:
    FLOOR_SPRITE = None
