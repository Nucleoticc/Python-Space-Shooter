import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game_set, screen, ship):
        Sprite.__init__(self)
        self.screen = screen
        self.game_set = game_set
        self.rect = pygame.Rect(0, 0, game_set.bullet_width, game_set.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_set.bullet_color
        self.speed = game_set.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
