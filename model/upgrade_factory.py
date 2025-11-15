from model.upgrade_strategy import AutoClickStrategy, MultiplierStrategy, NoOpStrategy
from model.upgrade import Upgrade


class UpgradeFactory:
    @staticmethod
    def create_strategy(data : dict):
        t = data["strategy"]

        if t == "autoclick":
            return AutoClickStrategy(cps=data.get("value", 0))

        if t == "multiplier":
            return MultiplierStrategy(multiplier=data.get("value", 0))

        return NoOpStrategy()

    @staticmethod
    def create_upgrade(data : dict):
        upgrades = []

        for item in data:
            strategy = UpgradeFactory.create_strategy(item)
            upgrade = Upgrade(
                name=item["name"],
                cost=item["cost"],
                strategy=strategy
            )
            upgrades.append(upgrade)

        return upgrades
