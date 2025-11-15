import pygame


class UiComponents:
    def __init__(self, x, y, h, w, call_back, data):
        self.rect = pygame.Rect(x, y, w, h)
        self.visible = True
        self.call_back = call_back
        self.data = data
        pass

    def draw(self, screen):
        pass

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def click(self):
        if self.call_back:
            self.call_back()