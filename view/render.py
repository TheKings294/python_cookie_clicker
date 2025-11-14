# view/renderer.py
import pygame

class Renderer:
    def __init__(self, screen, ui_manager, event_manager):
        self.screen = screen
        self.ui_manager = ui_manager
        self.event_manager = event_manager

        # Listen to model changes
        self.event_manager.subscribe("cookies_updated", self.on_cookies_updated)
        self.event_manager.subscribe("upgrade_progress", self.on_upgrade_progress)

    # ---------------------
    # Event callbacks
    # ---------------------

    def on_cookies_updated(self, amount):
        self.ui_manager.update_cookie_label(amount)

    def on_upgrade_progress(self, value):
        self.ui_manager.update_progress_bar(value)

    def draw(self):
        self.screen.fill((30, 30, 30))

        # Draw UI
        self.ui_manager.draw(self.screen)

        pygame.display.flip()
