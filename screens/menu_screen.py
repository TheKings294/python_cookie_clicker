from screens.base_screen import BaseScreen
import pygame
from view.button_components import Button


class MenuScreen(BaseScreen):
    def __init__(self, game_manager, event_manager, screen_manager, game_state):
        super().__init__(game_manager, event_manager, screen_manager, game_state)
        self.event_manager = event_manager
        self.screen_manager = screen_manager
        self.game_state = game_state

        self.play_button = Button(300, 200, 200, 60, "Play", self.ui_manager.font, self.play)
        #self.credits_button = Button(300, 300, 200, 60, "Credits", self.ui_manager.font, self.credits)
        self.quit_button = Button(300, 400, 200, 60, "Quit", self.ui_manager.font, self.quit_game)
        self.ui_manager.ui.extend([self.play_button, self.quit_button])

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        self.ui_manager.draw(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ui_manager.handle_click(*event.pos)

    def play(self): self.screen_manager.set_screen("game")

    #def credits(self): self.screen_manager.set_screen("credits")

    def quit_game(self): import sys; sys.exit()
