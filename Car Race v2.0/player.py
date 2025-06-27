import pygame


running = True
pause_game = False
class Player:
    def __init__(self) -> None:
        self.player = pygame.image.load("assets/img/player.png")
        self.crash = pygame.image.load("assets/img/crash.png")
        self.car_hit = pygame.mixer.Sound("assets/sounds/carhit.wav")
        self.player_rect = self.player.get_rect()
        self.player_rect.x , self.player_rect.y = (265,500)
        self.speed = 0
        self.speed_font = pygame.font.Font("EvilEmpire.ttf",30)

        
    
    def move_player(self):
        global running,pause_game
        pause_game=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pause_game = True

                if event.key == pygame.K_a:
                    if 370 < self.player_rect.x < 500:
                        self.player_rect.x -= 130

                    elif 240 < self.player_rect.x < 370:
                        self.player_rect.x -= 130
                
                elif event.key == pygame.K_d:
                    
                    if 240 < self.player_rect.x < 370:
                        self.player_rect.x += 130

                    elif 100 < self.player_rect.x < 240:
                        self.player_rect.x += 130

                elif event.key == pygame.K_w:
                    self.speed += 1
                
                elif event.key == pygame.K_s:
                    self.speed -= 1
                    
    def return_speed(self):
        r_speed =self.speed
        self.speed = 0
        return  self.speed #r_speed

    def return_running(self):
        return running

    def return_pause_game(self):
        return pause_game

    def write_speed(self,screen,fps):
        if fps < 32:
            fps = 31
        text_speed = self.speed_font.render(f"Km/h:{fps-30}", True, (255, 215, 0))
        screen.blit(text_speed,(490,0))

    def draw_player(self,screen):
        screen.blit(self.player,self.player_rect)


    def collide_car(self,vehicles_rect_list,screen):  
           
        if self.player_rect.collidelistall(vehicles_rect_list):
            screen.blit(self.crash,self.player_rect)
            pygame.mixer.Sound.play(self.car_hit)
            return 1
    
    def return_player_rect(self):
        return self.player_rect
