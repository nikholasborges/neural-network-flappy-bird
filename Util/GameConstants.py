import os
import pygame
from win32api import GetSystemMetrics


class Global:
    WIDTH = 800
    # get the system screen height dynamically
    HEIGHT = GetSystemMetrics(1) - 60

    BACKGROUND_SPRITE = os.path.join('.\\Resources\\img', 'background.png')

    FONT = os.path.join('.\\Resources', 'EightBitDragon-anqx.ttf')


class Bird:
    MAX_ROTATION = 18
    ROTATION_VELOCITY = 5
    JUMP_HEIGHT = -8
    DISPLACEMENT_LIMIT = 10
    DEFAULT_DRAW_X_AXIS = 450
    DEFAULT_DRAW_Y_AXIS = 500

    BIRD_SPRITE_DICT = {'1': [os.path.join('.\\Resources\\img', 'yellow-bird-0.png'),
                              os.path.join('.\\Resources\\img', 'yellow-bird-1.png'),
                              os.path.join('.\\Resources\\img', 'yellow-bird-2.png'),
                              os.path.join('.\\Resources\\img', 'yellow-bird-3.png')],
                        '2': [os.path.join('.\\Resources\\img', 'blue-bird-0.png'),
                              os.path.join('.\\Resources\\img', 'blue-bird-1.png'),
                              os.path.join('.\\Resources\\img', 'blue-bird-2.png'),
                              os.path.join('.\\Resources\\img', 'blue-bird-3.png')],
                        '3': [os.path.join('.\\Resources\\img', 'green-bird-0.png'),
                              os.path.join('.\\Resources\\img', 'green-bird-1.png'),
                              os.path.join('.\\Resources\\img', 'green-bird-2.png'),
                              os.path.join('.\\Resources\\img', 'green-bird-3.png')],
                        '4': [os.path.join('.\\Resources\\img', 'purple-bird-0.png'),
                              os.path.join('.\\Resources\\img', 'purple-bird-1.png'),
                              os.path.join('.\\Resources\\img', 'purple-bird-2.png'),
                              os.path.join('.\\Resources\\img', 'purple-bird-3.png')],
                        '5': [os.path.join('.\\Resources\\img', 'red-bird-0.png'),
                              os.path.join('.\\Resources\\img', 'red-bird-1.png'),
                              os.path.join('.\\Resources\\img', 'red-bird-2.png'),
                              os.path.join('.\\Resources\\img', 'red-bird-3.png')],
                        }


class Pipe:
    GAP = 190
    VELOCITY = 5
    DRAW_SPEED = 800

    PIPE_SPRITE = os.path.join('.\\Resources\\img', 'pipe.png')


class Floor:
    VELOCITY = 5
    DEFAULT_HEIGHT = 870

    FLOOR_SPRITE = os.path.join('.\\Resources\\img', 'floor.png')
