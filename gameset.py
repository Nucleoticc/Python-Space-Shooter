try:
    import pygame
except ImportError:
    import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.player_health = 3
        self.score = 0
        self.bullet_speed = 6
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (0, 0, 128)
        self.enbullet_width = 5
        self.enbullet_height = 25
        self.enbullet_color = (178, 34, 34)
        self.bullets_onscreen = 3
        self.fleet_direct = 1
        try:
            self.alien_images = (pygame.image.load('images/alien.png'),
                                 pygame.image.load('images/alien2.png'),
                                 pygame.image.load('images/alien3.png'))
        except FileNotFoundError:
            print(FileNotFoundError)
        try:
            self.icon = pygame.image.load('images/main.ico')
        except FileNotFoundError:
            print(FileNotFoundError)
        try:
            self.wallpaper = (pygame.image.load('images/wall1.jpg'),
                              pygame.image.load('images/wall2.jpg'),
                              pygame.image.load('images/wall3.jpg'))
        except FileNotFoundError:
            print(FileNotFoundError)
