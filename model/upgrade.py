from abc import ABC, abstractmethod

class Upgrade(ABC):
    def __init__ (self, name, cost):
        self.name = name
        self.cost = cost

    @abstractmethod
    def apply (self):
        pass

    @abstractmethod
    def can_buy (self):
        pass

class UniqueUpgrade(Upgrade):
    def __init__ (self, name, player, cost, effect):
        super().__init__(name, cost)
        self.purchased = False
        self.player = player
        self.effect = effect

    def can_buy (self):
        return not self.purchased and self.player.getmoney() >= self.cost

    def apply (self):
        if self.can_buy():
            self.player.subtract_money(self.cost)
            self.purchased = True

class LevelUpgrade(Upgrade):
    def __init__ (self, name, base_cost, ):
        super().__init__(name, base_cost)
