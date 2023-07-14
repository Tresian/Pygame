import pygame
from pygame.color import THECOLORS

class Object_(pygame.sprite.Sprite):
    def __init__(self,
                 position: tuple[int, int] = (0, 0),
                 size: tuple[int, int] = (50, 50)
                 ) -> None:
        
        self.screen = pygame.display.get_surface()

        self.position = position
        self.size = size

        self.rect = pygame.Rect((0, 0), self.size)
        self.rect.center = self.position

        self.image = pygame.Surface(self.size)
        self.image.fill(THECOLORS["green"])

    def control(self) -> None:

        self.input()
        self.draw()

    def input(self) -> None: 
        
        self.mouse_position = pygame.mouse.get_pos()
        self.mouse_pressed = pygame.mouse.get_pressed()
        self.keys = pygame.key.get_pressed()

    def draw(self) -> None: self.screen.blit(self.image, self.rect)