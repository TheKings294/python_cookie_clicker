import os.path

from model.game_state import GameState
import json
from utils.list_to_json import upgrades_list_to_json, achievements_list_to_json
from utils.json_to_list import upgrades_json_to_list, achievements_json_to_list


class SaveManager():
    _save_path = ""

    def __init__(self, path: str):
        self._save_path = path

    def save(self, save: GameState):
        save_game_data = {
            "money": save.get_money(),
            "total_money": save.get_total_money_stat(),
            "money_per_click": save.get_money_per_click()
        }

        upgrade_data = upgrades_list_to_json(save.get_upgrades_list())
        achievements_data = achievements_list_to_json(save.get_achievements_list())

        with open(self._save_path + "/savegame.json", "w") as file:
            json.dump(save_game_data, file)

        ##with open(self._save_path + "/achievements.json", "w") as file:
        ##json.dump(achievements_data, file)

        ##with open(self._save_path + "/upgrades.json", "w") as file:
        ##json.dump(upgrade_data, file)

    def load(self) -> GameState:
        game_state = GameState()
        if not os.path.isdir(self._save_path):
            return game_state

        with open(self._save_path + "/savegame.json", "r") as file:
            data_s = json.load(file)

        ##with open(self._save_path + "/achievements.json", "r") as file:
        ##data_a = json.load(file)

        ##with open(self._save_path + "/upgrades.json", "r") as file:
        ##data_u = json.load(file)

        game_state.add_money(data_s["money"])
        game_state.set_total_money_stat(data_s["total_money"])
        game_state.set_money_per_click(data_s["money_per_click"])
        ##game_state.add_to_upgrades_list(upgrades_json_to_list(data_u))
        ##game_state.add_to_achievements_list(achievements_json_to_list(data_a))

        return game_state
