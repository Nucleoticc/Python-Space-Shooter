try:
    import pygame
    from pygame.sprite import Group
    from ship import Ship
    import gamefuncs as gaf
    from gameset import Settings
    import time
    import os
except ImportError:
    import pygame
    from pygame.sprite import Group
    from ship import Ship
    import gamefuncs as gaf
    from gameset import Settings
    import time
    import os
    print(ImportError)


class Run:
    def __init__(self, choice):
        x, y = 100, 30
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (x, y)
        pygame.init()
        pygame.font.init()
        self.game_set = Settings()
        self.screen = pygame.display.set_mode((self.game_set.screen_width, self.game_set.screen_height))
        self.game_set.alien_images[0].convert_alpha()
        self.game_set.alien_images[1].convert_alpha()
        self.game_set.alien_images[2].convert_alpha()
        self.game_set.wallpaper[0].convert()
        self.game_set.wallpaper[1].convert()
        self.game_set.wallpaper[2].convert()
        pygame.display.set_icon(self.game_set.icon)
        pygame.display.set_caption("Alien Invasion")
        pygame.mouse.set_visible(False)
        gaf.stages = 0
        gaf.aliens_dead = False
        self.ship = Ship(self.game_set, self.screen, choice)
        self.bullets = Group()
        self.aliens = Group()
        self.enemy_bullets = Group()
        gaf.create_fleet(self.game_set, self.screen, self.ship, self.aliens)
        self.game_running = True
        self.score_text = pygame.font.SysFont('Comic Sans MS', 20)
        self.Health_text = pygame.font.SysFont('Comic Sans MS', 20)
        self.game_over_text = pygame.font.SysFont('Comic Sans MS', 40)
        self.game_end = False
        self.clock = pygame.time.Clock()

    def run_game(self):
        while self.game_running:
            if gaf.check_events(self.game_set, self.screen, self.bullets, self.ship, self.enemy_bullets, self.aliens) == 0:
                self.game_running = False
                break
            self.ship.update()
            gaf.update_bullets(self.game_set, self.screen, self.ship, self.bullets, self.aliens)
            gaf.update_enbullets(self.game_set, self.screen, self.ship, self.enemy_bullets)
            gaf.update_aliens(self.game_set, self.aliens)
            gaf.update_screen(self.game_set, self.screen, self.ship, self.aliens, self.bullets, self.enemy_bullets)
            if gaf.end_game(self.game_set) == 0:
                self.game_running = False
                self.game_end = True
            self.clock.tick(60)
        while self.game_end:
            self.screen.fill(self.game_set.bg_color)
            pygame.event.pump()
            self.text_surface = self.game_over_text.render("GAME OVER", False, (192, 192, 192))
            self.screen.blit(self.text_surface, (470, 340))
            self.score_surface = self.game_over_text.render("Score: {}".format(float(self.game_set.score)), False, (192, 192, 192))
            self.screen.blit(self.score_surface, (470, 400))
            self.health_surface = self.game_over_text.render("Health: {}".format(self.game_set.player_health),
                                                             False, (192, 192, 192))
            self.screen.blit(self.health_surface, (470, 440))
            self.game_end = False
            pygame.display.flip()
            time.sleep(5)
        pygame.display.quit()
        return self.game_set.score
