from model.game_state import GameState


class Upgrade:
    def __init__(self, name, cost, strategy):
        self.name = name
        self.cost = cost
        self.strategy = strategy
        self.level = 0

    def can_buy(self, game_state: GameState):
        return game_state.get_money() >= self.cost

    def buy(self, game_state: GameState):
        if not self.can_buy(game_state):
            return False

        game_state.subtract_money(self.cost)
        self.level += 1

        # Apply the strategy effect
        self.strategy.apply(game_state, self.level)
        return True

    def update(self, game_state, dt):
        self.strategy.update(game_state, dt, self.level)