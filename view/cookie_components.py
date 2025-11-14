from view.ui_components import UiComponents
import pygame


class CookieComponent(UiComponents):
    def __init__(self, x, y, h, w, call_back, cookies):
        super().__init__(x, y, h, w, call_back)
        self.cookies = cookies

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        print(self.cookies)