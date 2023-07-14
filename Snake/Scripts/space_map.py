import pygame
from pygame.color import THECOLORS


class Map:

    COUNT_BLOCK = 20
    SIZE_BLOCK = 20
    MARGIN = 1
    HEADER_MARGIN = 70
    HEADER_COLOR = (48, 227, 202)

    indent = [SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK,
                SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK + HEADER_MARGIN]

    def __init__(self) -> None:
        
        self.screen = pygame.display.get_surface()

    def control(self): 
        for row in range(self.COUNT_BLOCK):
            for column in range(self.COUNT_BLOCK):
                if (row + column) % 2 == 0: self.color = THECOLORS['white']
                else: self.color = THECOLORS['purple']
                self.draw(self.color, row, column)

    def draw(self, color, row, column, /) -> None:
        pygame.draw.rect(self.screen, self.HEADER_COLOR, [0, 0, self.indent[0], self.HEADER_MARGIN])

        pygame.draw.rect(self.screen, color, 
                        (self.SIZE_BLOCK + column*self.SIZE_BLOCK + self.MARGIN*(column + 1), 
                         self.HEADER_MARGIN + self.SIZE_BLOCK + row*self.SIZE_BLOCK + self.MARGIN*(row + 1),
                         self.SIZE_BLOCK, self.SIZE_BLOCK))

