import pygame

from core.game_manager import GameManager


class EventHandler:
    def __init__(self, game_manager: GameManager):
        self.game_manager = game_manager

    def handle_click(self, x, y):
        self.game_manager.handle_click(x, y)

    def handle_key_press(self, key):
         if key == pygame.K_s:
             self.game_manager.save_game()