import pygame
from constants import *

class Scarecrow(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        # Call parent constructor:
        pygame.sprite.Sprite.__init__(self)

        # Make Surface to put sprite on:
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)

        # Draw sprite to the surface:
        # TODO: Replace with pixel art:
        pygame.draw.circle(self.image, (255, 50, 50), (TILE_SIZE // 2, TILE_SIZE // 2), 6)

        # Set starting position:
        self.pos_x = starting_position[0] * TILE_SIZE + TILE_SIZE // 2
        self.pos_y = starting_position[1] * TILE_SIZE + TILE_SIZE // 2
        
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pos_x), int(self.pos_y))
