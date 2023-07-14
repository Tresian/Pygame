import pygame
from pygame.color import THECOLORS

from tield import Tield



class Map:
    
    COUNT_TIELD = 25
    MARGIN = 1

    def __init__(self) -> None:

        self.screen = pygame.display.get_surface()

        self.tield_list = []
        self.create_map()
    
    def control(self) -> None: self.draw()

    def create_map(self) -> None: 

        for row in range(self.COUNT_TIELD):
            self.tield_list.append([])
            for column in range(self.COUNT_TIELD):
                if (row + column) % 2 == 0: self.tield_list[row].append(Tield(row, column, "white"))
                else: self.tield_list[row].append(Tield(row, column, "purple"))

        #print(len(self.tield_list), self.tield_list)

    def draw(self) -> None: 
        for row in self.tield_list:
            for column in row: 
                column.draw()
        