# plane.py

import pygame
from pygame.sprite import Sprite
from pygame import Color
from i_plane import IPlane


class Plane(Sprite, IPlane):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/plane.png").convert()
        self.image = pygame.transform.scale(self.image, (80, 80))

        color_key: Color = self.image.get_at((0, 0))
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 530)

    def update(self):
        ...
        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        # if self.rect.left > 0:
        #     if pressed_keys[K_LEFT]:
        #         self.rect.move_ip(-5, 0)
        # if self.rect.right < SCREEN_WIDTH:
        #     if pressed_keys[K_RIGHT]:
        #         self.rect.move_ip(5, 0)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

    def move_left(self) -> None:
        self.rect.centerx -= 5

    def move_right(self) -> None:
        self.rect.centerx += 5
