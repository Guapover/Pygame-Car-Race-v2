import pygame


green = (0,120,0)


class Road:
    def __init__(self):
        self.line_1 = pygame.Rect(225, 0, 12, 60)
        self.line_2 = pygame.Rect(225, 150, 12, 60)
        self.line_3 = pygame.Rect(225, 300, 12, 60)
        self.line_4 = pygame.Rect(225, 450, 12, 60)
        self.line_5 = pygame.Rect(225, 600, 12, 60)

        self.line_6 = pygame.Rect(365, 0, 12, 60)
        self.line_7 = pygame.Rect(365, 150, 12, 60)
        self.line_8 = pygame.Rect(365, 300, 12, 60)
        self.line_9 = pygame.Rect(365, 450, 12, 60)
        self.line_10 = pygame.Rect(365, 600, 12, 60)


        self.line_list = [self.line_1,self.line_2,self.line_3,self.line_4,self.line_5, self.line_6, self.line_7, self.line_8, self.line_9, self.line_10]

        self.road = pygame.Surface((400,700))
        self.road.fill((50,50,50))

        self.road_left = pygame.Surface((20,700))
        self.road_left.fill((70,70,70))

        self.road_right = pygame.Surface((20,700))
        self.road_right.fill((70,70,70))
    
    def draw_road(self,screen):
        screen.fill(green)
        screen.blit(self.road,(100,0))

        screen.blit(self.road_left,(90,0))

        screen.blit(self.road_right,(490,0))


    
    def draw_lines(self,screen):
        for line in self.line_list:
            line.y += 3
            pygame.draw.rect(screen, (135,135,135), line)
            if line.y > 700:
                line.y = -55