'''
Created on Nov 7, 2022

@author: Samia Azme
'''
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    
    def __init__(self, admin_game):
        super(). __init__()
        self.screen = admin_game.screen
        self.settings = admin_game.settings
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = admin_game.skiff.rect.midtop
        self.y = float(self.rect.y) 
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) 
           
            
    
    
    