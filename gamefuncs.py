try:
    from bullet import Bullet
    from enemybullets import EnemyBullet
    from alien import Alien
    import pygame
    import random
except ImportError:
    from bullet import Bullet
    from enemybullets import EnemyBullet
    from alien import Alien
    import pygame
    import random

stages = 0
aliens_dead = False
Delay_Shoot = pygame.USEREVENT + 1
pygame.time.set_timer(Delay_Shoot, 350)


def check_events(game_set, screen, bullets, ship, enemybullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movement_right = True
            elif event.key == pygame.K_LEFT:
                ship.movement_left = True
            elif event.key == pygame.K_SPACE:
                if len(bullets) < game_set.bullets_onscreen:
                    new_bullet = Bullet(game_set, screen, ship)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movement_right = False
            elif event.key == pygame.K_LEFT:
                ship.movement_left = False
        elif event.type == Delay_Shoot:
            create_enbullets(game_set, screen, enemybullets, aliens)


def update_screen(game_set, screen, ship, aliens, bullets, enemybullets):
    screen.blit(game_set.wallpaper[stages], (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for enbullet in enemybullets.sprites():
        enbullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(game_set, screen, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            game_set.score -= 0.5
    check_collision_player(game_set, screen, ship, aliens, bullets)


def check_collision_player(game_set, screen, ship, aliens, bullets):
    global stages, aliens_dead
    collide = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for _ in collide:
        game_set.score += 10
    if stages == 0:
        if len(aliens) == 0:
            bullets.empty()
            stages += 1
            create_fleet(game_set, screen, ship, aliens)
    elif stages == 1:
        if len(aliens) == 0:
            bullets.empty()
            stages += 1
            create_fleet(game_set, screen, ship, aliens)
    elif stages == 2:
        if len(aliens) == 0:
            aliens_dead = True


def num_alien(game_set, alien_width):
    alien_number = int((game_set.screen_width - (2 * alien_width)) / (2 * alien_width))
    return alien_number


def rows_alien(game_set, ship_height, alien_height):
    number_rows = int((game_set.screen_height - (3 * alien_height) - ship_height) / (2 * alien_height))
    return number_rows


def check_edges(game_set, aliens):
    for alien in aliens.sprites():
        if alien.hit_edges():
            change_direct(game_set)
            break


def change_direct(game_set):
    game_set.fleet_direct *= -1


def create_alien(game_set, screen, aliens, alien_num, row_num):
    alien = Alien(game_set, screen)
    alien.changesprite(game_set, stages)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_num)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height = (2 * alien.rect.height * row_num)
    aliens.add(alien)


def create_fleet(game_set, screen, ship, aliens):
    alien = Alien(game_set, screen)
    alien_number = num_alien(game_set, alien.rect.width)
    alien_rows = rows_alien(game_set, ship.rect.height, alien.rect.height)
    for rows in range(alien_rows):
        for alien_num in range(alien_number):
            create_alien(game_set, screen, aliens, alien_num, rows)


def update_aliens(game_set, aliens):
    check_edges(game_set, aliens)
    aliens.update()


def create_enbullets(game_set, screen, enemybullets, aliens):
    if aliens:
        enemy = random.choice(aliens.sprites())
        new_enbullet = EnemyBullet(game_set, screen, enemy)
        enemybullets.add(new_enbullet)


def update_enbullets(game_set, screen, ship,  enemy_bullets):
    enemy_bullets.update()
    screen_rect = screen.get_rect()
    for enbullet in enemy_bullets.copy():
        if enbullet.rect.top > screen_rect.bottom:
            enemy_bullets.remove(enbullet)
    check_collision_enemy(game_set, ship, enemy_bullets)


def check_collision_enemy(game_set, ship, enemy_bullets):
    if pygame.sprite.spritecollide(ship, enemy_bullets, True):
        game_set.player_health -= 1


def end_game(game_set):
    if game_set.player_health == 0 or aliens_dead == True:
        return 0
