from screens.base_screen import BaseScreen


class ScreenManager:
    def __init__(self):
        self.curent_screen : BaseScreen = None
        self.screens : dict[str, BaseScreen] = []


    def add_screen(self, screen, name):
        self.screens.update({name: screen})

    def set_screen(self, screen: str):
        self.curent_screen = self.screens[screen]

    def update(self, dt):
        self.curent_screen.update(dt)

    def draw(self, screen):
        self.curent_screen.draw(screen)

    def handle_event(self, event):
        self.curent_screen.handle_event(event)

    def handle_click(self, x, y):
        self.curent_screen.ui_manager.handle_click(x, y)