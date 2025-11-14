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

        # Font
        #self.font = pygame.font.Font(None, 30)

        self.cookie_label = CookieComponent(10, 10, 50, 50, self.on_click_cookie, game_state.get_money())

        # Register components
        self.ui.extend([
            self.cookie_label,
            #self.cookie_button,
            #self.upgrade_bar,
        ])

    def update_cookie_label(self, amount):
        self.cookie_label.cookies = amount

    def draw(self, screen):
        for element in self.ui:
            element.draw(screen)

    def handle_click(self, x, y):
        for element in self.ui:
            if element.is_hovered((x, y)):
                element.click()

    def on_click_cookie(self):
        self.event_manager.notify("click_cookie", None)