from model.upgrade import Upgrade
from model.upgrade_factory import UpgradeFactory


def upgrades_json_to_list(data) -> list:
    return UpgradeFactory().create_upgrade(data)
