## Money = arme
    ## Money par seconde
## Click = combien de money par click
## Upgrades list
## Achievement list

class GameState:
    _money: int = 0
    _money_per_click: int = 0
    _total_money_stat: int = 0
    _upgrades_list: list = []
    _achievements_list: list = []

    def get_money(self):
        return self._money

    def add_money(self, money):
        self._money += money
        self.add_total_money_stat(money)

    def subtract_money(self, money):
        self._money -= money

    def get_money_per_click(self):
        return self._money_per_click

    def add_money_per_click(self, money_per_click):
        self._money_per_click += money_per_click

    def subtract_money_per_click(self, money_per_click):
        self._money_per_click -= money_per_click

    def get_total_money_stat(self):
        return self._total_money_stat

    def add_total_money_stat(self, money):
        self._total_money_stat += money

    def set_total_money_stat(self, money):
        self._total_money_stat = money

    def get_achievements_list(self):
        return self._achievements_list

    def add_to_achievements_list(self, achievements):
        self._achievements_list.append(achievements)

    def get_upgrades_list(self):
        return self._upgrades_list

    def add_to_upgrades_list(self, upgrade):
        self._upgrades_list.append(upgrade)