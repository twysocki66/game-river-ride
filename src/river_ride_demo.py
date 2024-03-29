# river_ride_demo.py

import pygame
from game import Game
from background import Background
from plane import Plane
from event_dispatcher import EventDispatcher


def main():
    game = Game("River ride DEMO", framerate=60)
    game.set_random()

    bg = Background(game.get_display())
    game.set_background(bg)

    plane = Plane()
    game.set_plane(plane)

    # game.add_sprite(plane)

    dispatcher = EventDispatcher()
    dispatcher.add_handler(pygame.KEYDOWN, pygame.K_LEFT, game.plane_move_left_handler)
    dispatcher.add_handler(
        pygame.KEYDOWN, pygame.K_RIGHT, game.plane_move_right_handler
    )
    dispatcher.add_handler(pygame.KEYUP, pygame.K_UP, game.bg_speed_inc)
    dispatcher.add_handler(pygame.KEYUP, pygame.K_DOWN, game.bg_speed_dec)
    game.set_event_dispatcher(dispatcher)

    game.loop()


if __name__ == "__main__":
    main()
