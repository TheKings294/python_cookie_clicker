from model.upgrade import Upgrade
from model.upgrade_strategy import AutoClickStrategy


def upgrades_list_to_json(upgrades: list[Upgrade]):
    upgrades_data = []
    for upgrade in upgrades:
        upgrades_data = {
            "name": upgrade.name,
            "cost": upgrade.cost,
            "strategy" : upgrade.strategy.name,
            "value" : upgrade.strategy.cps
                        if isinstance(upgrade.strategy, AutoClickStrategy)
                        else upgrade.strategy.multiplier
        }

    return upgrades_data
