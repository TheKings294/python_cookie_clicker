import pygame
from view.ui_components import UiComponents

class Button(UiComponents):
    def __init__(self, x, y, w, h, text, font, call_back,
                 bg_color=(70, 130, 180), hover_color=(100, 160, 210), text_color=(255,255,255)):
        super().__init__(x, y, h, w, call_back)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

        self.visible = True

    def draw(self, screen):
        if not self.visible:
            return

        print("button draw")
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.is_hovered(mouse_pos) else self.bg_color

        # Draw button rectangle
        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        # Render text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if self.is_hovered(event.pos):
                self.click()
