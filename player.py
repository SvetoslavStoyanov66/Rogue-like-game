import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height): 
        super().__init__()
        self.image = pygame.image.load("Assets/Sprites/Player/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))

    def draw(self,surface):
        surface.blit(self.image, self.rect)
