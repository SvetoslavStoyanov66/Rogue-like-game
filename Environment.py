from os import walk
from typing import List
import pygame
import random
 

class Environment:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.all_enemies = List
        self.background = pygame.image.load('Assets/Sprites/Ground.webp')
        self.bg_width = 1792 
        self.bg_hight = 1024
        self.bg_x = 0
        self.bg_y = 0
        self.initialize_envirinment()

    def initialize_envirinment(self):
        for _ in range(10):
            square = Enemy("Assets/Sprites/Square.png")
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
        surface.blit(self.background, (-self.bg_x ,-self.bg_y))
        surface.blit(self.background, (-self.bg_x + self.bg_width,-self.bg_y))
        surface.blit(self.background, (-self.bg_x + -self.bg_width,-self.bg_y))
        surface.blit(self.background, (-self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background, (-self.bg_x,self.bg_hight + -self.bg_y))
        surface.blit(self.background, (self.bg_width + -self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background, (-self.bg_width + -self.bg_x,-self.bg_hight + -self.bg_y))
        surface.blit(self.background, (self.bg_width + -self.bg_x,self.bg_hight + -self.bg_y))
        surface.blit(self.background, (-self.bg_width + -self.bg_x,self.bg_hight + -self.bg_y))
        self.all_sprites.draw(surface)




class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, random_position = True):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 3  
        self.moving = True

        if random_position:
            # Position the sprite at a random location on the screen
            screen_size = pygame.display.get_surface().get_size()
            num = random.randint(1,4)
            if num == 1:
                self.rect.x = -100
                self.rect.y = random.randint(0,screen_size[1])
            elif num == 2:
                self.rect.x = screen_size[0] + 100
                self.rect.y = random.randint(0,screen_size[1])

            elif num == 3:
                self.rect.x = random.randint(0,screen_size[0])
                self.rect.y = screen_size[1] + 100

            elif num == 4:
                self.rect.x = random.randint(0,screen_size[0])
                self.rect.y = -100


       
    def update(self):
        screen_size = pygame.display.get_surface().get_size()
        screen_center = (screen_size[0] / 2, screen_size[1] / 2)

        if self.moving:
            direction = pygame.math.Vector2(screen_center) - self.rect.center
            if direction.length() > 0:
                direction = direction.normalize()
                self.rect.center += direction * self.speed
                self.rect.clamp_ip(pygame.Rect(0, 0, *screen_size))
 
