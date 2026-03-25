import pygame
from constants import *

class LookoutTower:
    def __init__(self, position):
        self.grid_x, self.grid_y = position
    
    def draw(self, surface):
        center_x = self.grid_x * TILE_SIZE + TILE_SIZE // 2
        center_y = self.grid_y * TILE_SIZE + TILE_SIZE // 2

        pygame.draw.circle(surface, (255, 255, 50), (center_x, center_y), 6) # yellow