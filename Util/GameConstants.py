import os
import pygame


class Global:
    WIDTH = 800
    HEIGHT = 1000

    BACKGROUND_SPRITE = os.path.join('.\\Resources\\img', 'background.png')


class Bird:
    MAX_ROTATION = 18
    ROTATION_VELOCITY = 5
    JUMP_HEIGHT = -8
    DISPLACEMENT_LIMIT = 10
    DEFAULT_DRAW_X_AXIS = 450
    DEFAULT_DRAW_Y_AXIS = 500

    BIRD_SPRITE = [os.path.join('.\\Resources\\img', 'bird-0.png'),
                   os.path.join('.\\Resources\\img', 'bird-1.png'),
                   os.path.join('.\\Resources\\img', 'bird-2.png'),
                   os.path.join('.\\Resources\\img', 'bird-3.png')]


class Pipe:
    GAP = 190
    VELOCITY = 5
    DRAW_SPEED = 800

    PIPE_SPRITE = os.path.join('.\\Resources\\img', 'pipe.png')


class Floor:
    VELOCITY = 5
    DEFAULT_HEIGHT = 870

    FLOOR_SPRITE = os.path.join('.\\Resources\\img', 'floor.png')
