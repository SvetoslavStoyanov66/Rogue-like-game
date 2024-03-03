import pygame
import random

class Environment:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.background = StaticSprite('Assets/Sprites/Ground.webp')
        self.bg_width = 1792 
        self.bg_hight = 1024
        self.bg_x = 0
        self.bg_y = 0
        self.initialize_envirinment()

    def initialize_envirinment(self):
        for _ in range(10):
            square = StaticSprite("Assets/Sprites/Square.png")
            self.all_sprites.add(square)
    
    def move(self,dx, dy):
        self.bg_x += dx
        self.bg_y += dy
        if self.bg_x >= self.bg_width:
           self.bg_x = 0
        if self.bg_x <= -self.bg_width:
           self.bg_x = 0
        if self.bg_y >= self.bg_hight:
           self.bg_y = 0
        if self.bg_y <= -self.bg_hight:
           self.bg_y = 0
        for sprite in self.all_sprites:
           sprite.rect.x -= dx
           sprite.rect.y -= dy




    def draw(self, surface):
        surface.blit(self.background.image, (-self.bg_x ,-self.bg_y))
        surface.blit(self.background.image, (-self.bg_x + self.bg_width,-self.bg_y))
        surface.blit(self.background.image, (-self.bg_x + -self.bg_width,-self.bg_y))
        surface.blit(self.background.image, (-self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background.image, (-self.bg_x,self.bg_hight + -self.bg_y))
        surface.blit(self.background.image, (self.bg_width + -self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background.image, (-self.bg_width + -self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background.image, (self.bg_width + -self.bg_x,self.bg_hight + -self.bg_y))
        surface.blit(self.background.image, (-self.bg_width + -self.bg_x,self.bg_hight + -self.bg_y))
        self.all_sprites.draw(surface)




class StaticSprite(pygame.sprite.Sprite):
    def __init__(self, image_file, random_position = False):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

        if random_position:
            # Position the sprite at a random location on the screen
            screen_size = pygame.display.get_surface().get_size()
            self.rect.x = random.randint(0, screen_size[0])
            self.rect.y = random.randint(0, screen_size[1])
