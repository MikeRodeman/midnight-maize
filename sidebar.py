import pygame
from constants import *
from player import *

class Sidebar:
    def __init__(self):
        # Start where the maze ends at the right.
        self.rect = pygame.Rect(MAZE_WIDTH, 0, SIDEBAR_WIDTH, LOGICAL_SCREEN_HEIGHT)

        # None picks the default OS font:
        self.font = pygame.font.SysFont(None, 16)
    
    def draw(self, surface, player):
        pygame.draw.rect(surface, SIDEBAR_COLOR, self.rect)

        stamina_str = f"Stamina: {int(player.stamina)}%"

        text_color = (255, 50, 50) if player.is_exhausted else WHITE

        text_surface = self.font.render(stamina_str, False, text_color)

        text_x = self.rect.x + 10
        text_y = 20
        surface.blit(text_surface, (text_x, text_y))