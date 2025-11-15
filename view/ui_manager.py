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

        self.font = pygame.font.Font("./assets/arial.ttf", 25)


    def draw(self, screen):
        for element in self.ui:
            element.draw(screen)

    def handle_click(self, x, y):
        for element in self.ui:
            if element.is_hovered((x, y)):
                if element.data is not None:
                    element.click_btn(element.data)
                else:
                    element.click()

    def on_click_cookie(self):
        self.event_manager.notify("click_cookie", None)

