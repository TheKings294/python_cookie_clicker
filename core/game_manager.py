import sys

import pygame

from controller.event_handler import EventHandler
from controller.input_manager import InputManager
from core.constant import Constant
from core.event_manager import EventManager
from core.save_manager import SaveManager
from core.screen_manager import ScreenManager
from model.game_state import GameState
from view.render import Renderer
from view.ui_manager import UIManager
from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen


class GameManager:
    pygame.init()
    _instance = None
    running: bool = False
    game_state = GameState()
    event_manager = EventManager()
    input_manager = {}
    save_manager = SaveManager("./data")
    screen_manager = ScreenManager()
    clock = pygame.time.Clock()

    screen = {}

    def __init__(self):
        self._instance = self
        self.input_manager = InputManager(EventHandler(self._instance))
        self.event_manager.subscribe("click_cookie", self.on_cookie_clicked)
        self.event_manager.subscribe("new_game", self.new_game)

    def start(self):
        print("Starting game...")
        self.screen = pygame.display.set_mode((Constant.width, Constant.height))
        pygame.display.set_caption("Click'n'Gun")
        self.screen_manager.screens = {
            "menu": MenuScreen(self, self.event_manager, self.screen_manager, self.game_state),
            "game": GameScreen(self, self.event_manager, self.screen_manager, self.game_state),
            #"credits": CreditsScreen(self.screen_manager)
        }

        self.screen_manager.set_screen("menu")
        self.load_game()
        self.running = True
        self.game_loop()

    def game_loop(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.save_game()
                    self.running = False
                    sys.exit()
                else:
                    self.screen_manager.handle_event(event)

            self.screen.fill((30, 30, 30))

            self.screen_manager.update(dt)
            self.screen_manager.draw(self.screen)

            pygame.display.flip()

    def update(self):
        pass

    def save_game(self):
        self.save_manager.save(self.game_state)

    def load_game(self):
        self.game_state = self.save_manager.load()
        if not self.game_state.is_good_healthy():
            raise Exception("Error during loading save")

    def new_game(self, data):
        self.save_manager.create_file_and_dir()
        self.game_state = GameState()
        self.save_game()

    def get_instance(self):
        return self

    def handle_click(self, x, y):
        self.screen_manager.handle_click(x, y)
        pass

    def on_cookie_clicked(self):
        self.game_state.add_money(self.game_state.get_money_per_click())
        self.event_manager.notify("cookies_updated", self.game_state.get_money())
        print(self.game_state.get_money())
