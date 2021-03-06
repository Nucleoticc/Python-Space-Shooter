try:
    import pygame
except ImportError:
    import pygame


class Ship:
    def __init__(self, game_set, screen, choice):
        self.screen = screen
        self.game_set = game_set
        self.choice = choice
        self.image = (pygame.image.load("images/spaceship.png").convert_alpha(),
                      pygame.image.load('images/spaceship1.png').convert_alpha(),
                      pygame.image.load('images/spaceship2.png').convert_alpha())
        self.rect = self.image[self.choice].get_rect()
        self.screen_rect = screen.get_rect()
        self.movement_right = False
        self.movement_left = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image[self.choice], self.rect)

    def update(self):
        if self.movement_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 4
        if self.movement_left == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 4
