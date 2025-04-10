import pygame
from config import GRAVITY, JUMP_POWER, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT  # Valores definidos no config.py

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_idle = pygame.image.load("../assets/Player.png").convert_alpha()
        self.image_walk = pygame.image.load("../assets/Player_2.png").convert_alpha()
        self.image_idle = pygame.transform.scale(self.image_idle, (85,85))
        self.image_walk = pygame.transform.scale(self.image_walk, (85,85))

        self.image = self.image_idle
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.velocity_x = 0  # Movimento horizontal
        self.velocity_y = 0  # Movimento vertical
        self.speed = PLAYER_SPEED  
        self.jump_power = -JUMP_POWER 
        self.gravity = GRAVITY 
        self.on_ground = False 

        
        self.vida = 3  
        self.estrelas = 0 
        self.blinking = False
        self.blink_counter = 0
        self.has_collided = False

    def update(self, keys, ground_rect):
        self.velocity_x = 0  
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed 
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed 

        self.rect.x += self.velocity_x
        self.check_boundaries() 

        if not self.on_ground:
            self.velocity_y += self.gravity
        else:
            self.velocity_y = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False 
        
        if self.velocity_x != 0:
            self.image = self.image_walk
        else:
            self.image = self.image_idle

        self.rect.y += self.velocity_y
        self.check_ground_collision(ground_rect)

        if self.blinking:
            self.blink_counter += 1
            if self.blink_counter % 10 < 5:
                self.image.set_alpha(128) 
            else:
                self.image.set_alpha(255)  
            if self.blink_counter > 120:  
                self.blinking = False
                self.image.set_alpha(255)
                self.blink_counter = 0

    def check_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > SCREEN_WIDTH:  
            self.rect.right = SCREEN_WIDTH  

    def check_ground_collision(self, ground_rect):
        if self.rect.colliderect(ground_rect):
            self.rect.bottom = ground_rect.top  
            self.on_ground = True 

    def collect(self, collectable):
        collectable.apply_effect(self)
