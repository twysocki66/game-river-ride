# game.py

import sys
import pygame
import random
from i_background import IBackground
from i_plane import IPlane
from i_event_dispatcher import IEventDispatcher


class Game:
    def __init__(
        self,
        caption: str = "Pygame Demo",
        display_size: (int, int) = (800, 600),
        framerate: float = 60.0,
        random_seed: bool = True,
    ) -> None:
        pygame.init()
        pygame.font.init()

        if random_seed:
            random.seed(100)

        self.__framerate = framerate
        self.__FPS = pygame.time.Clock()

        self.__display_size = display_size
        self.__display = pygame.display.set_mode(size=self.__display_size)

        pygame.display.set_caption(caption)

        self.__active = True

        self.__background: IBackground = None
        self.__plane: IPlane = None
        self.__dispatcher: IEventDispatcher = None

    def __debug_key_print(self, key):
        match key:
            case pygame.K_UP:
                print(f"Key UP: {key}")
            case pygame.K_DOWN:
                print(f"Key DOWN: {key}")
            case _:
                print(f"Key: {key}")

    def get_display(self):
        return self.__display

    def set_background(self, background: IBackground):
        self.__background = background

    def bg_speed_inc(self, arg):
        self.__background.speed_inc()

    def bg_speed_dec(self, arg):
        self.__background.speed_dec()

    def set_plane(self, plane: IPlane):
        self.__plane = plane

    def plane_move_left_handler(self, arg):
        self.__plane.move_left()

    def plane_move_right_handler(self, arg):
        self.__plane.move_right()

    # def add_sprite(self, sprite: ISprite):
    #   self.__sprites.append(sprite)
    #   ...

    def set_event_dispatcher(self, dispatcher: IEventDispatcher):
        self.__dispatcher = dispatcher
        self.__dispatcher.add_handler(pygame.QUIT, pygame.K_ESCAPE, self.quit_handler)
        self.__dispatcher.add_handler(pygame.KEYUP, pygame.K_ESCAPE, self.quit_handler)

        # self.__dispatcher.add_handler(
        #     pygame.KEYUP,
        #     pygame.K_UP,
        #     self.__debug_key_print,
        # )
        # self.__dispatcher.add_handler(
        #     pygame.KEYUP,
        #     pygame.K_DOWN,
        #     self.__debug_key_print,
        # )

    def quit_handler(self, arg=0):
        self.__active = False

    def loop(self):
        while self.__active:
            # Cycles through all occurring events
            if self.__dispatcher:
                self.__dispatcher.loop()

            if self.__background:
                self.__background.update()

            # for sprite in self.__sprites:
            #     sprite.draw(self.__display)
            self.__plane.draw(self.__display)

            pygame.display.update()

            # pygame.time.delay(200)
            self.__FPS.tick(self.__framerate)

        pygame.quit()
        sys.exit()
