import os

import pygame
from pygame.color import THECOLORS



class Display:

    BACKGROUND_COLOR = "black"

    def __init__(self,
                 name: str,
                 fullscreen: bool = False,
                 fps: int = 60,
                 size: tuple[int, int] = (700, 700)
                 ) -> None:
        os.system("cls")
        pygame.init()

        self.name = name
        self.fullscreen = fullscreen
        self.fps = fps
        self.size = size

        # self.size = pygame.display.get_desktop_sizes()[0]

        if self.fullscreen: self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        else: self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.name)

        self.icon = pygame.image.load('./Images/Icon/icon.jpg')
        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()

    def update(self, frame_color: str | tuple = BACKGROUND_COLOR) -> None:

        pygame.display.update()

        if isinstance(frame_color, str): self.screen.fill(THECOLORS[frame_color])
        elif isinstance(frame_color, tuple): self.screen.fill(frame_color)

        self.clock.tick(self.fps)


