import pygame
from view.ui_components import UiComponents


class ImageComponent(UiComponents):
    def __init__(self, x, y, w, h, image_path, call_back=None):
        super().__init__(x, y, w, h, call_back, None)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.visible = True

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
