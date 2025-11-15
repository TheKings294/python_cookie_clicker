from core.event_manager import EventManager
from model.game_state import GameState
from screens.base_screen import BaseScreen
import pygame
from view.button_components import Button
from view.image_components import ImageComponent
from view.text_component import TextComponent


class GameScreen(BaseScreen):
    def __init__(self, game_manager, event_manager, screen_manager, game_state):
        super().__init__(game_manager, event_manager, screen_manager, game_state)
        self.event_manager: EventManager = event_manager
        self.screen_manager = screen_manager
        self.game_state: GameState = game_state

        self.cookie_image = ImageComponent(300, 200, 200, 100, "assets/weapon.png", self.click_on_gun)
        self.cookie_text = TextComponent(100, 100, 200, 100, "Cookies : " + str(self.game_state.get_money()))
        self.ui_manager.ui.extend([self.cookie_image, self.cookie_text])
        self.ui_manager.ui.extend(self.do_btn_for_upgrade())

        self.event_manager.subscribe("cookie_updated", self.cookie_text.set_text)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, dt):
        self.game_manager.lunch_upgrade(dt)

    def draw(self, surface):
        self.ui_manager.draw(surface)

    def do_btn_for_upgrade(self):
        start_y = 20
        btn = []
        for i, u in enumerate(self.game_manager.upgrades_available):
            btn.append(Button(625, start_y + 70 * i, 150, 50, u.name + ' ' + str(u.level), None,
                              self.click_on_upgrade, u))

        return btn

    def click_on_gun(self):
        self.event_manager.notify("click_cookie", None)

    def click_on_upgrade(self, u):
        self.event_manager.notify("upgrade", u)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ui_manager.handle_click(*event.pos)
