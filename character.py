import pygame

class Character:
    def __init__(self, xpos, ypos, size, wheredraw):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.wheredraw = wheredraw

    def draw(self):
        pygame.draw.rect(self.wheredraw, "green", (self.xpos, self.ypos, 50*self.size, 20*self.size))

    def move(self, direction, speed):
        if direction == "UP":
            self.ypos += speed
        elif direction == "DOWN":
            self.ypos -= speed
        elif direction == "RIGHT":
            self.xpos += speed
        elif direction == "LEFT":
            self.xpos -= speed 

