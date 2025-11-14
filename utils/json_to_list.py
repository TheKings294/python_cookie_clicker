from model.upgrade import Upgrade
from model.upgrade_factory import UpgradeFactory


def upgrades_json_to_list(data) -> list:
    upgrade_list = []
    for u in data:
        upgrade = UpgradeFactory().create_upgrade(u)
        upgrade_list.append(upgrade)
        pass

    return upgrade_list
