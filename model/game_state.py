class GameState:
    _money: int = 0
    _money_per_click: int = 1
    _total_money_stat: int = 0
    _upgrades_list: list = []
    tab_upgrades = dict()

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

    def set_money_per_click(self, money_per_click):
        self._money_per_click = money_per_click

    def subtract_money_per_click(self, money_per_click):
        self._money_per_click -= money_per_click

    def get_total_money_stat(self):
        return self._total_money_stat

    def add_total_money_stat(self, money):
        self._total_money_stat += money

    def set_total_money_stat(self, money):
        self._total_money_stat = money


    def get_upgrades_list(self):
        return self._upgrades_list

    def add_to_upgrades_list(self, upgrade):
        self._upgrades_list.append(upgrade)

    def is_good_healthy(self):
        if not self._total_money_stat < 0 or not self._money < 0 and self._money_per_click == 1:
            return True
        return False
