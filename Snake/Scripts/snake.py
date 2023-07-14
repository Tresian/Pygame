import pygame

from object import Object_


class Snake(Object_):

    SPEED = 2

    def __init__(self,
                 position: tuple[int, int] = (0, 0),
                 size: tuple[int, int] = (20, 20)
                 ) -> None:
        super().__init__(position, size)

        self.x_speed = 0
        self.y_speed = 0

    def control(self) -> None:
        super().control()

        self.input()
        self.move()

    def input(self) -> None:

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:    self.x_speed, self.y_speed =  0, -self.SPEED
        if self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:  self.x_speed, self.y_speed =  0,  self.SPEED
        if self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:  self.x_speed, self.y_speed = -self.SPEED,  0
        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]: self.x_speed, self.y_speed =  self.SPEED,  0

    def move(self) -> None:
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        if self.rect.left > self.screen.get_width(): self.rect.right = 0
        if self.rect.right < 0: self.rect.left = self.screen.get_width()

        if self.rect.bottom < 0: self.rect.top = self.screen.get_height()
        if self.rect.top > self.screen.get_height(): self.rect.bottom = 0

        