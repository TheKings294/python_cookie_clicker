import pygame
from view.ui_components import UiComponents

class Button(UiComponents):
    def __init__(self, x, y, w, h, text, font, call_back, data_click,
                 bg_color=(70, 130, 180), hover_color=(100, 160, 210), text_color=(255,255,255)):
        super().__init__(x, y, h, w, call_back, data_click)
        self.text = text
        self.font = font or pygame.font.Font('assets/arial.ttf', 15)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

        self.visible = True

    def draw(self, screen):
        if not self.visible:
            return

        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.is_hovered(mouse_pos) else self.bg_color

        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered(event.pos):
                self.click()

    def click_btn(self, data):
        self.call_back(data)