try:
    from pygame.sprite import Sprite
except ImportError:
    from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game_set, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.game_set = game_set
        self.image = game_set.alien_images[0]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def hit_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        self.x += (1.5 * self.game_set.fleet_direct)
        self.rect.x = self.x

    def changesprite(self, game_set, stages):
        self.image = game_set.alien_images[stages]
