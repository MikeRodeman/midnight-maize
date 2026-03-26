import pygame
from constants import *
from maze import *

class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        # Call parent constructor:
        pygame.sprite.Sprite.__init__(self)

        # Make Surface to put sprite on:
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)

        # Draw sprite to the surface:
        # TODO: Replace with pixel art:
        pygame.draw.circle(self.image, (50, 50, 255), (TILE_SIZE // 2, TILE_SIZE // 2), 6)

        # Set starting position:
        self.pos_x = starting_position[0] * TILE_SIZE + TILE_SIZE // 2
        self.pos_y = starting_position[1] * TILE_SIZE + TILE_SIZE // 2
        
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pos_x), int(self.pos_y))

        self.speed = 1.2 # TODO: Put in constants.py?
        

    def update(self, maze):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_UP] or keys[pygame.K_w]: dy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += self.speed

        # Move horizontally:
        self.pos_x += dx
        self.rect.centerx = int(self.pos_x)
        # self.handle_collision(maze, "horizontal", dx)

        # Move vertically:
        self.pos_y += dy
        self.rect.centery = int(self.pos_y)
        # self.handle_collision(maze, "vertical", dy)
    
    # def handle_collision(self, maze, axis, delta):
    #     for wall in maze.wall_rects:
    #         if self.rect.

