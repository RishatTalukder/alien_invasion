"""
Created on Oct 28, 2022

@author: Samia Azme
"""
import sys
import pygame

from settings import Settings
from Skiff import Skiff
from bullet import Bullet
from extraneous import Extraneous

clock = pygame.time.Clock()

class Administrator:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Extraneous Onslaught")
        self.skiff = Skiff(self)
        self.bullets = pygame.sprite.Group()
        self.extraneouses = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            clock.tick(60)
            self._check_events()
            self.skiff.update()
            self._update_bullets()
            self._update_extraneous()
            self._update_screen()

    def _check_events(self):
        for cases in pygame.event.get():
            if cases.type == pygame.QUIT:
                sys.exit()
            elif cases.type == pygame.KEYDOWN:
                self._check_keydown_cases(cases)
            elif cases.type == pygame.KEYUP:
                self._check_keyup_cases(cases)

    def _check_keydown_cases(self, cases):
        if cases.key == pygame.K_q:
            sys.exit()
        elif cases.key == pygame.K_SPACE:
            self._fire_bullet()

        if cases.key == pygame.K_RIGHT:
            self.skiff.moving_right = True
        elif cases.key == pygame.K_LEFT:
            self.skiff.moving_left = True
        if cases.key == pygame.K_UP:
            self.skiff.moving_up = True
        elif cases.key == pygame.K_DOWN:
            self.skiff.moving_down = True

    def _check_keyup_cases(self, cases):
        if cases.key == pygame.K_RIGHT:
            self.skiff.moving_right = False
        elif cases.key == pygame.K_LEFT:
            self.skiff.moving_left = False
        if cases.key == pygame.K_UP:
            self.skiff.moving_up = False
        elif cases.key == pygame.K_DOWN:
            self.skiff.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))
        
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.extraneouses, True, True
        )

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.skiff.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.extraneouses.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self):
        extraneous = Extraneous(self)
        extraneous_width, extraneous_height = extraneous.rect.size
        available_space_x = self.settings.screen_width - (2 * extraneous_width)
        number_extraneous_x = available_space_x // (2 * extraneous_width)
        skiff_height = self.skiff.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * extraneous_height) - skiff_height
        )

        number_rows = available_space_y // (2 * extraneous_height)

        for row_number in range(number_rows):
            for extraneous_number in range(number_extraneous_x):
                self._creat_extraneous(extraneous_number, row_number)

    def _update_extraneous(self):
        self._check_fleet_edges()
        self.extraneouses.update()

    def _creat_extraneous(self, extraneous_number, row_number):

        extraneous = Extraneous(self)
        extraneous_width, extraneous_height = extraneous.rect.size
        extraneous.x = extraneous_width + 2 * extraneous_width * extraneous_number
        extraneous.rect.x = extraneous.x
        extraneous.rect.y = (
            extraneous.rect.height + 2 * extraneous.rect.height * row_number
        )
        self.extraneouses.add(extraneous)

    def _check_fleet_edges(self):

        for extraneous in self.extraneouses.sprites():
            if extraneous.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):

        for extraneous in self.extraneouses.sprites():
            extraneous.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1


if __name__ == "__main__":

    admin = Administrator()
    admin.run_game()
