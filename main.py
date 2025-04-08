import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from collectables import * # BoloDeRolo, Pitu, Estrela
import random

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

    pontuacao = font.render(f"Estrelas: {player.estrelas}", True, (0,0,0))
    pontuacao_rect = pontuacao.get_rect(center=(65,30))
    screen.blit(pontuacao, pontuacao_rect)

    num = random.randint(1,100)
    object_position_x = random.randint(30, 380)
    object_position_y = random.randint(30, 200)
    if num == 1:
        object = random.choice(['bolo de rolo', 'pitu', 'estrela'])
        if object == 'bolo de rolo':
            BoloDeRolo(object_position_x, object_position_y)
        elif object == "pitu":
            Pitu(object_position_x, object_position_y)
        elif object == "estrela":
            Estrela(object_position_x, object_position_y)
    
    '''
    # Colisão entre o coletável e o personagem:
    if player.colliderect(object_position_x):
        # Objeto desaparece
    '''
    pygame.display.flip()
    clock.tick(60)