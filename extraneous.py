'''
Created on Nov 12, 2022

@author: Samia Azme
'''
import pygame
from pygame.sprite import Sprite

class Extraneous(Sprite):
    def __init__(self, admin_game):
        super().__init__()
        self.screen = admin_game.screen
        self.settings = admin_game.settings
        
        self.image = pygame.image.load('Images/ufo-g105caaac6_6140.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    
    def update(self):
        
        self.x += (self.settings.extraneous_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    
