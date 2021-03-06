import pygame
from pygame.sprite import Sprite


class EnemyBullet(Sprite):
    def __init__(self, game_set, screen, enemyaliens):
        Sprite.__init__(self)
        self.screen = screen
        self.game_set = game_set
        self.rect = pygame.Rect(0, 0, game_set.enbullet_width, game_set.enbullet_height)
        self.rect.centerx = enemyaliens.rect.centerx
        self.rect.top = enemyaliens.rect.top

        self.y = float(self.rect.y)

        self.color = game_set.enbullet_color
        self.speed = game_set.bullet_speed

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)