import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height): 
        super().__init__()
        self.spritesWalking = []
        self.spritesIdle = []
        self.load_sprites(self.spritesWalking,"walk")
        self.load_sprites(self.spritesIdle,"idle")
        self.current_sprite = 0
        self.image = self.spritesWalking[self.current_sprite]
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        self.facing_right = True
        self.animatingWalking = False

    def load_sprites(self,listName,name):
        for i in range(1, 7):  
            sprite = pygame.image.load(f"Assets/Sprites/Player/{name}{i}.png").convert_alpha()
            new_width = sprite.get_width() * 3
            new_height = sprite.get_height() * 3
            listName.append(pygame.transform.scale(sprite, (new_width, new_height)))
    def animate(self):
        end = 6  
        self.current_sprite += 0.1  
        if self.current_sprite >= end: self.current_sprite = 0

        if self.animatingWalking:
           new_image = self.spritesWalking[int(self.current_sprite)]
        else:
           new_image = self.spritesIdle[int(self.current_sprite)]

        if not self.facing_right:
           new_image = pygame.transform.flip(new_image, True, False)

        self.image = new_image  

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        self.animatingWalking = keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]

        if self.animatingWalking:
            if keys[pygame.K_a]:
               self.facing_right = False
            elif keys[pygame.K_d]:
               self.facing_right = True

        self.animate()
    def draw(self,surface):
        surface.blit(self.image, self.rect)
