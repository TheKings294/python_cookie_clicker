from view.ui_components import UiComponents
import pygame
from pygame import Surface


class CookieComponent(UiComponents):
    def __init__(self, x, y, h, w, call_back, cookies):
        super().__init__(x, y, h, w, call_back)
        self.cookies = cookies
        self.font = pygame.font.Font("./assets/arial.ttf", 20)
        self.text : Surface = self.font.render(f"Cookie: {self.cookies}", True, (255, 255, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        if self.text is not None:
            screen.blit(self.text, self.rect)

