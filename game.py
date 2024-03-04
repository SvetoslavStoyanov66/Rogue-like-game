import pygame
from Environment import Environment, Enemy
from player import Player
from pygame.math import Vector2
import math
pygame.init()

# Set up the screen
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Window")


# Create game objects
environment = Environment()
player = Player(screen_width, screen_height)
player_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # Check for keys pressed
    keys = pygame.key.get_pressed()
    movement = Vector2(0, 0)

    if keys[pygame.K_w]:
        movement.y -= player_speed  # Move up
    if keys[pygame.K_s]:
        movement.y += player_speed  # Move down
    if keys[pygame.K_a]:
        movement.x -= player_speed # Move left
    if keys[pygame.K_d]:
        movement.x += player_speed # Move right
    if movement.x != 0 and movement.y != 0:
        movement.x /= math.sqrt(2)
        movement.y /= math.sqrt(2)

    environment.move(movement.x, movement.y)   
    
    player.update()
        # Render
    screen.fill((0, 0, 0))
    environment.draw(screen)
    for enemy in environment.all_sprites:
        enemy.update()
    player.draw(screen)
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
