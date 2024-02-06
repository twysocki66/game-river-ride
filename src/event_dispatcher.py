# event_dispatcher.py

import pygame
from i_event_dispatcher import IEventDispatcher


class EventDispatcher(IEventDispatcher):
    """
    Use example:
        self.events = EventDispatcher()\n
        self.events.add_handler(pygame.QUIT, pygame.K_ESCAPE, self.events.quit_handler)\n
        self.events.add_handler(pygame.KEYUP, pygame.K_ESCAPE, self.events.quit_handler)\n
        \n
        self.events.add_handler(pygame.KEYUP, pygame.K_UP, any_handler_fun_1)\n
        self.events.add_handler(pygame.KEYDOWN, pygame.K_LEFT, any_handler_fun_2)\n
        \n
        def any_handler_fun_1(arg):\n
            ...
    """

    def __init__(self, key_repeat_delay=80, key_repeat_interval=25) -> None:
        self.__key_repeat_delay = key_repeat_delay
        self.__key_repeat_interval = key_repeat_interval

        self.__handlers_quit: list[function] = []
        self.__handlers_keydown: dict[int, list[function]] = {}
        self.__handlers_keyup: dict[int, list[function]] = {}

    def add_handler(self, event_type: int, event_key: int, handler_fun) -> None:
        """
        Possible values for 'event_type': pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP.
        """
        match event_type:
            case pygame.QUIT:
                self.__handlers_quit.append(handler_fun)
            case pygame.KEYDOWN:
                if not event_key in self.__handlers_keydown:
                    self.__handlers_keydown[event_key] = []
                self.__handlers_keydown[event_key].append(handler_fun)
            case pygame.KEYUP:
                if not event_key in self.__handlers_keyup:
                    self.__handlers_keyup[event_key] = []
                self.__handlers_keyup[event_key].append(handler_fun)

    def _dispatch(self, event_type: int, event_key: int) -> None:
        match event_type:
            case pygame.QUIT:
                for handler in self.__handlers_quit:
                    handler()
            case pygame.KEYDOWN:
                if event_key in self.__handlers_keydown:
                    for handler in self.__handlers_keydown[event_key]:
                        handler(event_key)
            case pygame.KEYUP:
                if event_key in self.__handlers_keyup:
                    for handler in self.__handlers_keyup[event_key]:
                        handler(event_key)

    def loop(self) -> None:
        pygame.key.set_repeat(self.__key_repeat_delay, self.__key_repeat_interval)
        for event in pygame.event.get():
            key = event.key if "key" in event.dict else 0
            self._dispatch(event.type, key)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     paddle.move_ip(0, -7)
        # if keys[pygame.K_DOWN]:
        #     paddle.move_ip(0, 7)
