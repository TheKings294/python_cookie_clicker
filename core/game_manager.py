import sys

import pygame

from controller.event_handler import EventHandler
from controller.input_manager import InputManager
from core.constant import Constant
from core.event_manager import EventManager
from core.save_manager import SaveManager
from model.game_state import GameState


class GameManager:
    _instance = {}
    running: bool = False
    game_state = GameState()
    event_manager = EventManager()
    ui_manager = {}
    input_manager = {}
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
        self.game_state = self.save_manager.load()
        print(self.game_state.get_total_money_stat())
        self.event_manager.subscribe("score_update", self.on_score_update)
        self.event_manager.subscribe("player_death", self.on_player_death)
        print(self.event_manager.listener_list)
        self.running = True
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

            self.screen.fill((0, 0, 0))
            pygame.display.flip()

    def update(self):
        pass

    def save_game(self):
        pass

    def load_game(self):
        pass

    def get_instance(self):
        return self

    def handle_click(self, x, y):
        pass

    def on_score_update(self, data):
        print(f"🎯 Score updated: {data['score']}")

    def on_player_death(self, data):
        print(f"💀 Player {data['player_name']} has died.")
