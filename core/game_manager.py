import sys

import pygame

from core.constant import Constant
from core.save_manager import SaveManager
from model.game_state import GameState


class GameManager:
    _instance = {}
    running: bool = False
    game_state = {}
    event_manager = {}
    ui_manager = {}
    input_manager = {}
    save_manager = SaveManager("./data")

    screen = {}

    def __init__(self):
        pass

    def start(self):
        print("Starting game...")
        pygame.init()
        self.screen = pygame.display.set_mode((Constant.width, Constant.height))
        pygame.display.set_caption("Click'n'Gun")
        self.game_state = self.save_manager.load()
        print(self.game_state.get_total_money_stat())
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
