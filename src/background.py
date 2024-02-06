# background.py

import pygame
import random
from i_background import IBackground


class Background(IBackground):
    def __init__(self, display: pygame.Surface):
        self.__display = display
        self.__display_rect = display.get_rect()

        self.__peace_water = pygame.image.load(
            "image/background/bg_water_25x25.png"
        ).convert()
        self.__peace_grass = pygame.image.load(
            "image/background/bg_grass_25x25.png"
        ).convert()
        self.__peace_rect = self.__peace_water.get_rect()
        self.__peace_width = self.__peace_rect.width
        self.__peace_height = self.__peace_rect.height

        self.__buffer_stock = self.__peace_height * 2

        self.__buffer_rect = self.__display_rect
        self.__buffer_rect.height += self.__buffer_stock
        self.__buffer_size = (self.__buffer_rect.width, self.__buffer_rect.height)
        self.__buffer = pygame.Surface(self.__buffer_size)

        self.__window_rect = self.__buffer_rect
        self.__window_rect.top = self.__buffer_stock
        self.__window_rect.bottom = self.__buffer_rect.height + self.__buffer_stock

        self.__peace_h_count = self.__buffer_rect.width // self.__peace_width
        self.__peace_v_count = self.__buffer_rect.height // self.__peace_height

        self.__line_counter = 0
        self.__shift_y = 0

        self.__delay_counter = 0
        self.__speed_y = 2

        self.__init_buffer()

    def __init_line(self, counter: int = 0) -> pygame.Surface:
        line = pygame.Surface((self.__buffer_rect.width, self.__peace_height))

        water_sz = random.randint(6, 26)
        water_pos = (32 - water_sz) // 2

        for i in range(0, self.__peace_h_count):
            if i >= water_pos and i < water_pos + water_sz:
                line.blit(self.__peace_water, (i * self.__peace_width, 0))
            else:
                line.blit(self.__peace_grass, (i * self.__peace_width, 0))

        if counter > 0:
            self.__counter_stamp(line, counter)

        return line

    def __counter_stamp(self, line: pygame.Surface, counter: int):
        font = pygame.font.Font(pygame.font.get_default_font(), 15)

        color = (255, 0, 0)
        if counter > self.__peace_v_count:
            color = (0, 0, 255)

        text = font.render(f"LINE: {counter:04d}", True, color)
        line.blit(text, dest=(10, 5))

    def __init_buffer(self):
        for i in range(1, self.__peace_v_count + 1):
            self.__line_counter += 1
            self.__buffer.blit(
                self.__init_line(self.__line_counter),
                (0, self.__buffer_rect.height - i * self.__peace_height),
            )

    def __move(self, dx: int, dy: int):
        if dx != 0 or dy != 0:
            self.__buffer.scroll(dx, dy)
            self.__shift_y += dy

            if self.__shift_y == 25:
                self.__shift_y = 0
                self.__line_counter += 1
                self.__buffer.blit(
                    self.__init_line(self.__line_counter),
                    (0, 0),
                )

    def update(self):
        if self.__delay_counter < self.__speed_y:
            self.__delay_counter += 1
        else:
            self.__delay_counter = 0
            self.__move(0, 1)

            self.__display.blit(
                self.__buffer,
                (0, 0),
                self.__window_rect,
            )

    def speed_inc(self) -> None:
        if self.__speed_y > 0:
            self.__speed_y -= 1
            print(f"{self.__speed_y=}")

    def speed_dec(self) -> None:
        if self.__speed_y < 3:
            self.__speed_y += 1
            print(f"{self.__speed_y=}")
