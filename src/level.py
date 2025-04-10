import pygame

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_height = self.height - 50 
        self.setup_ground() 

    def setup_ground(self):
        ground_width = self.width
        ground_height = 50  


        self.ground = pygame.Rect(0, self.ground_height, ground_width, ground_height)

    def update(self):
        pass
