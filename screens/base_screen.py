from abc import ABC, abstractmethod
from view.ui_manager import UIManager


class BaseScreen(ABC):
    def __init__(self, game_manager, event_manager, screen_manager, game_state):
        self.game_manager = game_manager
        self.ui_manager = UIManager(event_manager, game_state)
        pass

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass