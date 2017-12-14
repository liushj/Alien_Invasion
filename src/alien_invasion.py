import pygame

from src.settings import Setting
from src.ship import Ship
import src.game_functions as game


def run_game():
    # initialize game and create a screen object
    pygame.init()
    # set window param
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # set ship param
    ship = Ship(screen, ai_setting)

    # start game main loop
    while True:
        game.check_events(ship)
        ship.update_move()
        game.update_screen(ai_setting, screen, ship)


run_game()

