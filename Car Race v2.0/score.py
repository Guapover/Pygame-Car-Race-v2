import pygame
import random

class Score:
    def __init__(self) -> None:
        self.score_font = pygame.font.Font("EvilEmpire.ttf",30)
        self.game_score = 0

        self.coin_collect_sound= pygame.mixer.Sound("assets/sounds/collectcoin.mp3")
        self.coin_img = pygame.image.load("assets/img/coin.png")
        self.roads = [130,265,400]
    
        self.coin_rect = self.coin_img.get_rect()
        self.coin_rect.x = random.choice(self.roads)
        self.coin_rect.y = -self.coin_rect.height
    
    def increase_score(self):
        self.game_score += 50
    
    def score_reduction(self):
        self.game_score -= 50

    def write_score(self,screen):
        text_score = self.score_font.render(f"SCORE:{self.game_score}", True, (255, 215, 0))
        screen.blit(text_score,(0,0))
    
    def coin(self,vehicle_number):
        if vehicle_number == 2:
            return 0
        return 1
    
    def coin_create(self,screen_height,vehicle_rect):
        if vehicle_rect.y >= screen_height:
            if vehicle_rect.x in self.roads:
                self.roads.remove(vehicle_rect.x)
            self.coin_rect.x = random.choice(self.roads)
            self.coin_rect.y = -vehicle_rect.height
            self.roads = [130,265,400]
    
    def collide_vehicle_coin(self,vehicle_rect):
        if vehicle_rect.x == self.coin_rect.x:
            self.roads.remove(vehicle_rect.x)
            self.coin_rect.x = random.choice(self.roads)
            self.roads = [130,265,400]


    def coin_draw(self,screen):
        self.coin_rect.y += 10
        screen.blit(self.coin_img,self.coin_rect)

    def collide_car(self,player_rect):
        if player_rect.colliderect(self.coin_rect):
            global vehicle_number
            self.game_score += 100
            vehicle_number = 2
            self.coin_rect.x = 1000 #görünmez yapsın
            pygame.mixer.Sound.play(self.coin_collect_sound)
        

