import pygame

class Projectile:
    def __init__(self, xpos, ypos, radius, color, vel):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color
        self.vel = vel

    def draw(self, wheredraw):
        pygame.draw.circle(wheredraw, self.color, (self.xpos, self.ypos), self.radius)
 
