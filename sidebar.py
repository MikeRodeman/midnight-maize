import pygame
import os
from constants import *
from player import *

class Sidebar:
    def __init__(self):
        # Start where the maze ends at the right.
        self.rect = pygame.Rect(MAZE_WIDTH, 0, SIDEBAR_WIDTH, LOGICAL_SCREEN_HEIGHT)

        font_path = "m5x7.ttf"

        if os.path.exists(font_path):
            self.font = pygame.font.Font(font_path, 16)
        else:
            # Fallback
            self.font = pygame.font.SysFont(None, 16)
    
    def draw(self, surface, player):
        pygame.draw.rect(surface, SIDEBAR_COLOR, self.rect)

        stamina_str = f"Stamina:\n{int(player.stamina)}%"

        text_color = (255, 50, 50) if player.is_exhausted else WHITE

        text_surface = self.font.render(stamina_str, False, text_color)

        surface.blit(text_surface, (self.rect.x + 5, 10))