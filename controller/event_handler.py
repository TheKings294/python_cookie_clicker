import pygame


class EventHandler:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def handle_click(self, x, y):
        self.game_manager.handle_click(x, y)

    def handle_key_press(self, key):
        if key == pygame.K_s:
            self.game_manager.save_game()
        elif key == pygame.K_w:
            self.game_manager.event_manager.notify("score_update", {"score": self.game_manager.game_state.get_money()})
            self.game_manager.event_manager.notify("player_death", {"player_name": "Alex"})
