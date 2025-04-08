import pygame

class Player(pygame.sprite.Sprite):
    #construtor
    def __init__(self, x, y):
        #herança - chama o construtor da classe pai (sprite)
        super().__init__()
        self.image = pygame.Surface((50, 50))  #cria um quadrado - enquanto ainda não temos sprite
        self.image.fill((0, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.velocity_x = 0 #horizontal
        self.velocity_y = 0 #vertical
        self.speed = 5 #velocidade base
        self.jump_power = -15  #valor negativo porque o eixo Y cresce para baixo
        self.gravity = 0.8 #gravidade
        self.on_ground = False 
        self.floor_y = y  #chão
        self.vida = 5
        self.estrelas = 0

    def update(self, *args, **kwargs):
        keys = kwargs.get("keys") 
        
        #horizontal
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
            
        #pulo (somente se estiver no chão pra não dar double jump)
        if keys[pygame.K_UP] and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False
        
        #gravidade
        self.velocity_y += self.gravity
        
        #atualizar posição
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        #verificar se atingiu o chão
        if self.rect.bottom >= self.floor_y:
            self.rect.bottom = self.floor_y
            self.velocity_y = 0
            self.on_ground = True