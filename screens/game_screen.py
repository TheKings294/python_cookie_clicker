from screens.base_screen import BaseScreen
import pygame
from view import ui_manager
from view.button_components import Button
from view.ui_manager import UIManager


class GameScreen(BaseScreen):
    def __init__(self, game_manager, event_manager, screen_manager, game_state):
        super().__init__(game_manager, event_manager, screen_manager, game_state)
        self.event_manager = event_manager
        self.screen_manager = screen_manager
        self.game_state = game_state

        self.cookie_button = Button(300, 200, 200, 60, "Cookie", self.ui_manager.font,game_manager.on_cookie_clicked)
        self.ui_manager.ui.extend([self.cookie_button])

    def enter(self):
        pass
    def exit(self):
        pass
    def update(self, dt):
        pass
    def draw(self, surface):
        self.ui_manager.draw(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ui_manager.handle_click(*event.pos)
