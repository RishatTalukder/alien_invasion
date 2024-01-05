'''
Created on Oct 29, 2022

@author: Samia Azme
'''
import pygame

class Skiff:
    def __init__(self, admin_game):
        self.screen = admin_game.screen
        self.settings = admin_game.settings
        self.screen_rect = admin_game.screen.get_rect()
        
        self.image = pygame.image.load('Images/rocket01.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.skiff_speed_x
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.skiff_speed_x
            
        self.rect.x = self.x
        
            
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.skiff_speed_y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.skiff_speed_y
        self.rect.y = self.y 
                   
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
       
            
        
        
        
        