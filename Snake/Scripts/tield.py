import pygame
from pygame.color import THECOLORS



class Tield:
    
    SIZE = 25

    def __init__(self, 
                 row: int,
                 column: int,
                 color: str | tuple[int, int, int]
                 ) -> None:
        self.screen = pygame.display.get_surface()

        self.row = row
        self.column = column
        self.color = color

    def control(self) -> None: self.draw()

    def draw(self) -> None: 
        pygame.draw.rect(self.screen, self.color, (self.SIZE + self.column*self.SIZE, 
                                                   self.SIZE + self.row*self.SIZE,
                                                   self.SIZE, self.SIZE))