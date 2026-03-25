import pygame
from constants import *

class Player:
    def __init__(self, starting_position):
        self.grid_x, self.grid_y = starting_position

    def draw(self, surface):
        center_x = self.grid_x * TILE_SIZE + TILE_SIZE // 2
        center_y = self.grid_y * TILE_SIZE + TILE_SIZE // 2

        pygame.draw.circle(surface, (50, 50, 255), (center_x, center_y), 6) # blue