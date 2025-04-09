import pygame
import random
from player import Player

# Classe com as funções principais dos objetos coletáveis:
class objeto_coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # self.image = image
        # self.rect = self.image.get_rect(center=(x, y))

    def update(self, *args, **kwargs):
        if self.rect.right < 0:
            self.kill()

    # Aplicando o efeito do objeto que foi coletado no jogador(classe player)
    def apply_efect(self, player):
        pass

# Subclasses para cada objeto específico:
class BoloDeRolo(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((30, 30))  #cria um quadrado - enquanto ainda não temos sprite
        self.image.fill((0, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        player.vida += 1
        print("Vida aumentada!")

class Pitu(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((30, 30))  #cria um quadrado - enquanto ainda não temos sprite
        self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        player.velocity_x += 2
        player.velocity_y += 2
        print("velocidade aumentada")

class Estrela(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((30, 30))  #cria um quadrado - enquanto ainda não temos sprite
        self.image.fill((0, 255, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        player.estrelas += 1
        print("Estrela obtida")