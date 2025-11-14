from screens.base_screen import BaseScreen
from view import ui_manager
from view.ui_manager import UIManager


class GameScreen(BaseScreen):
    def __init__(self, game_manager, event_manager, screen_manager, game_state):
        super().__init__(game_manager, event_manager, screen_manager, game_state)
        self.event_manager = event_manager
        self.screen_manager = screen_manager
        self.game_state = game_state

    def enter(self):
        pass
    def exit(self):
        pass
    def update(self, dt):
        pass
    def draw(self, surface):
        self.ui_manager.draw(surface)
    def handle_event(self, event):
        pass
