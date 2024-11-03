import random
import pygame
from circleshape import CircleShape

class Powerup(CircleShape):
    def __init__(x, y, radius):
        super().__init__(x, y, radius)
        self.__colors = ["green", "purple"]
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.__colors[random.randint(0, 1)], pygame.Rect())