import pygame
from core.constant import Constant
from core.event_manager import EventManager
from model.game_state import GameState
from view.cookie_components import CookieComponent
from view.ui_components import UiComponents


class UIManager:
    def __init__(self, event_manager, game_state: GameState):
        self.event_manager : EventManager = event_manager
        self.ui: list[UiComponents] = []
        self.game_state = game_state

        # Font
        self.font = pygame.font.Font("./assets/arial.ttf", 25)


    def draw(self, screen):
        print("Hi")
        for element in self.ui:
            element.draw(screen)

    def handle_click(self, x, y):
        for element in self.ui:
            if element.is_hovered((x, y)):
                element.click()

    def on_click_cookie(self):
        self.event_manager.notify("click_cookie", None)