import sys

import pygame

from src.settings import Setting


def run_game():
    # initialize game and create a screen object
    pygame.init()
    # setting parameter
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_setting.bg_color

    # start game main loop
    while True:
        # monitor keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # set background color
        screen.fill(bg_color)
        # make latest draw screen can be seen
        pygame.display.flip()


run_game()

