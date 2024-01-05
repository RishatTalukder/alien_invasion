'''
Created on Oct 29, 2022

@author: Samia Azme
'''
class Settings:
    
    def __init__(self):
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.skiff_speed_x = 5
        self.skiff_speed_y = 5
        
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9
        
        self.extraneous_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 means right, -1 means left
        self.fleet_direction = 1
        
        
    