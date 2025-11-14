import pygame
from .ui_components import UiComponents   # adjust import to your project structure

class TextComponent(UiComponents):
    def __init__(self, x, y, w, h, text, font_size=24, color=(255, 255, 255), call_back=None):
        super().__init__(x, y, w, h, call_back)

        self.text = text
        self.color = color
        self.font = pygame.font.Font("assets/arial.ttf", font_size)   # None = default system font

        self.render_text()

    def render_text(self):
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def set_text(self, new_text):
        self.text = str(new_text)
        self.render_text()

    def draw(self, screen):
        if not self.visible:
            return

        screen.blit(self.text_surface, self.text_rect)
