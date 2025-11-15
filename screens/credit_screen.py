import pygame
from screens.base_screen import BaseScreen
from view.button_components import Button


class CreditScreen(BaseScreen):
    def __init__(self, game_manager, event_manager=None, screen_manager=None, game_state=None):
        super().__init__(game_manager, event_manager, screen_manager, game_state)
        self.screen_manager = screen_manager
        self.font_title = pygame.font.Font(None, 60)
        self.font_text = pygame.font.Font(None, 36)

        self.credits = [
            "Jeu réalisé par :",
            "Antoine Gonsard - Enory D'Huysser",
            "",
            "Merci d'avoir joué !"
        ]

        # Bouton retour
        self.back_button = Button(
            50, 50, 150, 50,
            "Retour",
            self.font_text,
            lambda: self.screen_manager.set_screen("menu"),
            None
        )
        self.ui_manager.ui.append(self.back_button)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))  # fond noir

        title_surf = self.font_title.render("Crédits", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(surface.get_width() // 2, 100))
        surface.blit(title_surf, title_rect)

        start_y = 200
        for line in self.credits:
            text_surf = self.font_text.render(line, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(surface.get_width() // 2, start_y))
            surface.blit(text_surf, text_rect)
            start_y += 50  # espace entre les lignes

        self.ui_manager.draw(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ui_manager.handle_click(*event.pos)
