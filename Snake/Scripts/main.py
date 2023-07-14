import sys

import pygame

from display import Display
from map import Map
from snake import Snake


class Game:

    NAME = "Snake"
    AUTHOR = "TRES"

    def __init__(self) -> None:

        self.screen = Display(name=self.NAME)

        self.map = Map()
        
        self.main()

    def main(self) -> None:

        while True:
            self.handle_events()

            self.map.control()

            self.screen.update((120, 219, 226))

    def handle_events(self) -> None:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        

















if __name__ == "__main__": Game()