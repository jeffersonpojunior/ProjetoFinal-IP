import pygame

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_type):
        super().__init__()
        self.obstacle_type = obstacle_type
        if self.obstacle_type == 'jump': #obstaculo de chão
            self.image = pygame.image.load("../assets/Poca.png").convert_alpha()
        elif self.obstacle_type == 'crouch': #obstaculo voador
            self.image = pygame.image.load("../assets/Pombo_2.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.mask = pygame.mask.from_surface(self.image) 
        
        self.has_collided = False
        self.speed = 5

    def update(self, obstacles_speed):
        self.rect.x -= obstacles_speed

        if self.rect.right < 0:
            self.kill() 

    def apply_effect(self, player):
        if self.rect.colliderect(player.rect) and not self.has_collided:
            player.vida -= 1
            player.blinking = True
            player.blink_counter = 0
            self.has_collided = True

            if self.obstacle_type == 'jump':
                print("Obstáculo de pulo atingido!")
            elif self.obstacle_type == 'crouch':
                print("Obstáculo de agachamento atingido!")
    
