import pygame

import src.core.constants as c
from src.core.custom_types import Coordinate

class GlowStick(pygame.sprite.Sprite):
    """Represents a dropped glow stick that provides light and attracts the scarecrow."""
    def __init__(self, pixel_position: Coordinate) -> None:
        """Initializes a new glow stick at the given pixel coordinates.
        
        Args:
            pixel_position (Coordinate): The (x, y) pixel coordinates to place the glow stick.
        """
        super().__init__()

        # Pixel art:
        self.image = pygame.image.load(c.GRAPHICS_DIR / "glow_stick.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = pixel_position

        self.grid_x = pixel_position[0] // c.TILE_SIZE
        self.grid_y = pixel_position[1] // c.TILE_SIZE
        self.grid_position = (self.grid_x, self.grid_y)
