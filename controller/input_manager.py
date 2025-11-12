from controller.event_handler import EventHandler
import pygame


class InputManager:
    def __init__(self, event_handler: EventHandler):
        self.event_handler = event_handler

    def handle_event(self, event : pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.on_click(x, y)
        elif event.type == pygame.KEYDOWN:
            self.on_key_press(event.key)
        pass

    def on_click(self, x: int, y: int):
        self.event_handler.handle_click(x, y)
        pass

    def on_key_press(self, key: int):
        self.event_handler.handle_key_press(key)
        pass
