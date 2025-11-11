from abc import ABC, abstractmethod

class Upgrade(ABC):
    def __init__ (self, name, cost, player):
        self.name = name
        self.cost = cost
        self.player = player

    @abstractmethod
    def apply (self):
        pass

    @abstractmethod
    def can_buy (self):
        pass

    @abstractmethod
    def get_price (self):
        pass

class UniqueUpgrade(Upgrade):
    def __init__ (self, name, player, cost, effect):
        super().__init__(name, cost, player)
        self.purchased = False
        self.effect = effect

    def get_price(self):
        return self.cost

    def can_buy (self):
        return not self.purchased and self.player.getmoney() >= self.cost

    def apply (self):
        if self.can_buy():
            self.player.subtract_money(self.cost)
            self.purchased = True

class LevelUpgrade(Upgrade):
    def __init__ (self, name, base_cost, player, cost_multiplier, effect):
        super().__init__(name, base_cost, player)
        self.level = 0
        self.cost_multiplier = cost_multiplier
        self.effect = effect

    def get_price(self):
        return self.cost

    def can_buy (self):
        return self.player.getmoney() >= self.cost

    def apply (self):
        if self.can_buy():
            self.player.subtract_money(self.cost)
            self.cost *= self.cost_multiplier
            self.level += 1
