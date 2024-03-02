import pygame
from Environment import Environment
from player import Player

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
    if keys[pygame.K_w]:
        environment.move(0, -player_speed)  # Move environment down to simulate player moving up
    if keys[pygame.K_s]:
        environment.move(0, player_speed)  # Move environment up to simulate player moving down
    if keys[pygame.K_a]:
        environment.move(-player_speed, 0)  # Move environment right to simulate player moving left
    if keys[pygame.K_d]:
        environment.move(player_speed, 0)  # Move environment left to simulate player moving right

    player.update()
        # Render
    screen.fill((0, 0, 0))
    environment.draw(screen)
    player.draw(screen)
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
