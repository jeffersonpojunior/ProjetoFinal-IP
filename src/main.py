import pygame
import random
from level import Level
from player import Player
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from collectables import BoloDeRolo, Pitu, Estrela
from obstacles import Obstacles


class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("ReciRunner")
        self.clock = pygame.time.Clock()
        self.big_font = pygame.font.Font("freesansbold.ttf", 34)

        self.level = Level(screen_width, screen_height)
        self.player = Player(100, self.level.ground_height - 50) 

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.collects = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.game_active = False
        self.in_menu = True
        self.running = False

        self.coletavel_speed = 3 
        self.spawn_cooldown = 120
        self.spawn_timer = 0
        self.spawn_collectables()


    def spawn_collectables(self):
        #gera coletáveis aleatórios com chance em uma posição controlada
        if random.random() < 0.005:  # Probabilidade de gerar um novo coletável (ajuste conforme necessário)
            x = SCREEN_WIDTH + random.randint(50, 1000)
            y = random.randint(self.level.ground_height - 100, self.level.ground_height - 50)  
            collectable = random.choice([BoloDeRolo, Pitu, Estrela])(x, y)
            
            self.collects.add(collectable)  
            self.all_sprites.add(collectable) 

    def spawn_obstacles(self):
        if self.spawn_timer > 0:
            self.spawn_timer -= 1
            return  
        
        if random.random() < 0.5: 
            x = SCREEN_WIDTH + random.randint(100, 400) 
            obstacle_type = random.choice(['jump', 'crouch'])

            if obstacle_type == 'jump':
                y = self.level.ground_height - 25
            else:
                y = self.level.ground_height - 150

            obstacle = Obstacles(x, y, obstacle_type)
            self.obstacles.add(obstacle)
            self.all_sprites.add(obstacle)

            self.spawn_timer = random.randint(60, 120)  
            self.all_sprites.add(obstacle)  
            self.obstacles.add(obstacle)  

    def show_menu(self):
        #exibe o menu principal
        self.screen.fill((217, 154, 78))

        logo = pygame.image.load("../assets/Logo.png").convert()

        logo = pygame.transform.scale(logo, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(logo, (0, 0))
        font = pygame.font.Font(None, 36)
        

        start_text = font.render("Pressione 'Enter' para Iniciar", True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.35))
        self.screen.blit(start_text, start_rect)

        exit_text = font.render("Pressione 'ESC' para Sair", True, (0, 0, 0))
        exit_rect = exit_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 1.25))
        self.screen.blit(exit_text, exit_rect)

        pygame.display.flip()

    def handle_key_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game_active = True
                self.in_menu = False
            elif event.key == pygame.K_ESCAPE: 
                self.running = False
    
    def game_over(self):
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        
        score_text = font.render(f"Sombrinhas: {self.player.estrelas}", True, (255, 255, 255)) 
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        font_final = pygame.font.Font(None, 32)
        final_text = font_final.render(f"Pressione ESC para sair", True, (255, 255, 255)) 
        final_rect = final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        final_text_2 = font_final.render(f"Pressione qualquer tecla para reiniciar", True, (255, 255, 255)) 
        final_rect_2 = final_text_2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))

        self.screen.fill((0, 0, 0)) 
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(final_text, final_rect)
        self.screen.blit(final_text_2, final_rect_2)
        
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        waiting_for_input = False
                    else: 
                        self.restart_game()
                        waiting_for_input = False

    
    def restart_game(self):
        self.player.vida = 3 
        self.player.estrelas = 0  
        self.player.blinking = False  
        self.player.blink_counter = 0  
          
        self.level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)  
        self.player.rect.center = (100, self.level.ground_height - 50) 
        
        self.obstacles.empty() 
        self.collects.empty() 
        self.all_sprites.empty()  
        self.all_sprites.add(self.player) 

        self.coletavel_speed = 5  
        self.game_active = False  
        self.in_menu = True 
        self.spawn_cooldown = 120 
        self.spawn_timer = 0
        self.spawn_collectables() 
        self.spawn_obstacles()  

        print("Jogo reiniciado!")

    def update_game_state(self):
        keys = pygame.key.get_pressed()

        self.player.update(keys, self.level.ground)

        self.collects.update(coletavel_speed=self.coletavel_speed)

        self.obstacles.update(obstacles_speed=self.coletavel_speed)

        collected = pygame.sprite.spritecollide(self.player, self.collects, True)  
        for collectable in collected:
            if isinstance(collectable, Pitu):
                collectable.apply_effect(self) 
            else:
                collectable.apply_effect(self.player)  
        
        for obstacle in self.obstacles:
            obstacle.apply_effect(self.player)

        if self.player.vida <= 0:
            self.game_over()

        self.level.update()
        self.spawn_collectables()
        self.spawn_obstacles()

    def render_game(self, background):

        self.screen.blit(background, (0, 0)) 
        pygame.draw.rect(self.screen, (64, 120, 126), self.level.ground)

        if self.in_menu:
            self.show_menu()
        else:
            keys = pygame.key.get_pressed()  
            self.player.update(keys, self.level.ground) 
            self.collects.update(coletavel_speed=self.coletavel_speed) 
            self.all_sprites.draw(self.screen) 

            #HUD do jogo
            pontuacao = self.big_font.render(f"Sombrinhas: {self.player.estrelas}", True, (0,0,0))
            pontuacao_rect = pontuacao.get_rect(center=(SCREEN_WIDTH/2 - 80, 30))
            self.screen.blit(pontuacao, pontuacao_rect)
            vida = self.big_font.render(f"Vida: {self.player.vida}", True, (0,0,0))
            vida_rect = vida.get_rect(center=(60, 30))
            self.screen.blit(vida, vida_rect)
            velocidade = self.big_font.render(f"Velocidade: {(self.coletavel_speed/5)}x", True, (0,0,0))
            vel_rect = velocidade.get_rect(center=(SCREEN_WIDTH - 150, 30))
            self.screen.blit(velocidade, vel_rect)

        pygame.display.flip()


    def run(self):
        background = pygame.image.load("../assets/background.png").convert()
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.running = True  
        while self.running:


            for event in pygame.event.get():
                self.handle_key_events(event)

            if not self.in_menu and self.game_active:
                self.update_game_state() 

            self.render_game(background)  
            self.clock.tick(60) 


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
game.run()
