import pygame
from constants import *

class LookoutTower(pygame.sprite.Sprite):
    def __init__(self, position):
        # Call parent constructor:
        super().__init__()

        # Make Surface to put sprite on:
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)

        # Draw sprite to the surface:
        # TODO: Replace with pixel art:
        pygame.draw.circle(self.image, (255, 255, 50), (TILE_SIZE // 2, TILE_SIZE // 2), 6)

        # Set position:
        self.pos_x = position[0] * TILE_SIZE + TILE_SIZE // 2
        self.pos_y = position[1] * TILE_SIZE + TILE_SIZE // 2
        
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pos_x), int(self.pos_y))
