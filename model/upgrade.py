from core.event_manager import EventManager
from model.game_state import GameState


class Upgrade:
    def __init__(self, name, cost, strategy):
        self.name = name
        self.cost = cost
        self.strategy = strategy
        self.level = 1

    def can_buy(self, game_state: GameState):
        return game_state.get_money() >= self.cost

    def buy(self, game_state: GameState):
        if not self.can_buy(game_state):
            return False

        game_state.subtract_money(self.cost)
        self.level += 1
        self.cost = self.cost * 1.20

        self.strategy.apply(game_state, self.level)
        return True

    def update(self, game_state, dt, event_manager : EventManager):
        self.strategy.update(game_state, dt, self.level)
        event_manager.notify("cookie_updated", "Armes :" + str(round(game_state.get_money())))
        return True

    def set_level(self, level):
        self.level = level