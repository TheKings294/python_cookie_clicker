from model.game_state import GameState


class BaseUpgradeStrategy:
    def apply(self, game_state, level):
        pass

    def update(self, game_state, dt, level):
        pass


class AutoClickStrategy(BaseUpgradeStrategy):
    name = "autoclick"
    def __init__(self, cps: float):
        self.cps = cps

    def update(self, game_state, dt, level):
        game_state.cookies += self.cps * level * dt


class MultiplierStrategy(BaseUpgradeStrategy):
    name = "multiplier"
    def __init__(self, multiplier: float):
        self.multiplier = multiplier

    def apply(self, game_state : GameState, level):
        game_state.add_money_per_click(1 + self.multiplier * level)

class NoOpStrategy(BaseUpgradeStrategy):
    pass