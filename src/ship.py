import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        # initialize ship and set the beginning position
        self.screen = screen
        self.ai_settings = ai_settings
        # load ship image and get the rect
        self.image = pygame.image.load("../resources/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # set the beginning position of ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        # draw ship
        self.screen.blit(self.image, self.rect)

    def update_move(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        # with open("../doc/LogPosition.log", "a") as file_obj:
        #     file_obj.write(str(self.rect.centerx) + ", " + str(self.centerx))
        #     file_obj.write('\n')
