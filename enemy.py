import pygame

class Enemy():
    def __init__(self, xpos, ypos, color, size):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.size = size

    def draw (self, wheredraw):
        pygame.draw.rect(self.wheredraw, self.color, (self.xpos, self.ypos, self.size*10, self.size*10))
    