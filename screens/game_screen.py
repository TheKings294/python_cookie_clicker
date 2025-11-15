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

        self.cookie_image = ImageComponent(200, 200, 200, 100, "assets/weapon.png", self.click_on_gun)
        self.cookie_text = TextComponent(100, 100, 200, 100, "Armes : " + str(self.game_state.get_money()))
        self.ui_manager.ui.extend([self.cookie_image, self.cookie_text])
        self.btn = self.do_btn_for_upgrade()
        self.ui_manager.ui.extend(self.btn)

        self.event_manager.subscribe("cookie_updated", self.cookie_text.set_text)
        self.event_manager.subscribe("update_btn", self.update_all_btn)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, dt):
        self.game_manager.lunch_upgrade(dt)

    def draw(self, surface):
        self.ui_manager.draw(surface)

    def do_btn_for_upgrade(self):
        btn = []
        start_y = 20
        col_width = 180
        col_x_left = 440
        col_x_right = 440 + col_width

        for i, u in enumerate(self.game_manager.upgrades_available):
            col = i % 2
            row = i // 2

            x = col_x_left if col == 0 else col_x_right
            y = start_y + (row * 70)

            btn.append(Button(
                x, y, 150, 50,
                u.name + ' ' + str(u.level) + "\n" + "price:" + str(u.cost),
                None,
                self.click_on_upgrade,
                u
            ))

        return btn

    def click_on_gun(self):
        self.event_manager.notify("click_cookie", None)

    def click_on_upgrade(self, u, btn):
        self.event_manager.notify("upgrade", u)
        btn.text = u.name + " " + str(u.level + 1)

    def update_all_btn(self, data):
        print(data)
        for i, btn in enumerate(self.btn):
            name = self.game_manager.upgrades_available[i].name
            if name in data:
                level = data[name]
            else:
                level = 1

            btn.text = (str(name) + " " + str(level) + "\n" + "price: " + str(self.game_manager.upgrades_available[i].cost))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ui_manager.handle_click(*event.pos)
