import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

clock = pygame.time.Clock()

#config da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("teste")
font = pygame.font.Font(None, 36)

player = Player(400, 600)  #500 seria a posição Y do chão
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    all_sprites.update(keys=keys)
    
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)