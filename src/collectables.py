import pygame

class objeto_coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30)) 
        self.image.fill((0, 255, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, coletavel_speed):
        self.rect.x -= coletavel_speed 

        if self.rect.right < 0:
            self.kill()

    def apply_effect(self, player):
        pass  #subclasses irão definir o efeito específico


class BoloDeRolo(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("../assets/Bolo.png").convert_alpha()  
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        player.vida += 1
        print("Vida aumentada!")

class Pitu(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("../assets/Pitu.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, game):
        game.coletavel_speed += 2
        print("Velocidade aumentada")

class Estrela(objeto_coletavel):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("../assets/Sombrinha.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        player.estrelas += 1
        print(f"Estrela obtida. Estrelas: {player.estrelas}")
