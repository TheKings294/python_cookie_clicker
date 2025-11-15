import os.path

from model.game_state import GameState
import json
from utils.list_to_json import upgrades_list_to_json
from utils.json_to_list import upgrades_json_to_list


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

        if len(save.get_upgrades_list()) > 0:
            upgrade_data = upgrades_list_to_json(save.get_upgrades_list())
            with open(self._save_path + "/upgrades.json", "w") as file:
                json.dump(upgrade_data, file)
        else:
            with open(self._save_path + "/upgrades.json", "w") as file:
                json.dump([], file)

        with open(self._save_path + "/savegame.json", "w") as file:
            json.dump(save_game_data, file)


    def load(self) -> GameState:
        game_state = GameState()
        if (not os.path.isdir(self._save_path) or
                not os.path.isfile(self._save_path + "/savegame.json") or
                not os.path.isfile(self._save_path + "/upgrades.json")):
            return game_state

        with open(self._save_path + "/savegame.json", "r") as file:
            data_s = json.load(file)

        with open(self._save_path + "/upgrades.json", "r") as file:
            data_u = json.load(file)

        game_state.add_money(data_s["money"])
        game_state.set_total_money_stat(data_s["total_money"])
        game_state.set_money_per_click(data_s["money_per_click"])
        tab = {}
        for u in upgrades_json_to_list(data_u):
            if u.name in tab :
                tab[u.name] += 1
            else :
                tab[u.name] = 1

            game_state.add_to_upgrades_list(u)
        game_state.tab_upgrades = tab
        return game_state

    def create_file_and_dir(self):
        if not os.path.isdir(self._save_path):
            os.mkdir(self._save_path)
            open(self._save_path + "/savegame.json", "x").close()
            open(self._save_path + "/upgrades.json", "x").close()
