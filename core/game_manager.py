import sys

import pygame

from controller.event_handler import EventHandler
from controller.input_manager import InputManager
from core.constant import Constant
from core.event_manager import EventManager
from core.save_manager import SaveManager
from model.game_state import GameState
from view.render import Renderer
from view.ui_manager import UIManager


class GameManager:
    _instance = {}
    running: bool = False
    game_state = GameState()
    event_manager = EventManager()
    ui_manager = UIManager(event_manager, game_state)
    input_manager = {}
    render = {}
    save_manager = SaveManager("./data")

    screen = {}

    def __init__(self):
        self._instance = self
        self.input_manager = InputManager(EventHandler(self._instance))
        pass

    def start(self):
        print("Starting game...")
        pygame.init()
        self.screen = pygame.display.set_mode((Constant.width, Constant.height))
        pygame.display.set_caption("Click'n'Gun")
        self.load_game()
        print(self.game_state.get_total_money_stat())
        self.event_manager.subscribe("click_cookie", self.on_cookie_clicked)
        self.event_manager.subscribe("player_death", self.on_player_death)
        print(self.event_manager.listener_list)
        self.running = True
        self.render = Renderer(self.screen, self.ui_manager, self.event_manager)
        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.save_manager.save(self.game_state)
                    self.running = False
                    sys.exit()
                else:
                    self.input_manager.handle_event(event)

            self.render.draw()

    def update(self):
        pass

    def save_game(self):
        pass

    def load_game(self):
        self.game_state = self.save_manager.load()
        if not self.game_state.is_good_healthy():
            raise Exception("Error during loading save")

    def get_instance(self):
        return self

    def handle_click(self, x, y):
        self.ui_manager.handle_click(x, y)
        pass

    def on_cookie_clicked(self, data):
        self.game_state.add_money(self.game_state.get_money_per_click())
        self.event_manager.notify("cookies_updated", self.game_state.get_money())

    def on_player_death(self, data):
        print(f"💀 Player {data['player_name']} has died.")
