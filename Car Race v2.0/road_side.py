import pygame
import random


class Road_side:
    def __init__(self,x,y):
        self.tree_decor = pygame.image.load("assets/img/tree.png")
        self.tree_decor_rect = self.tree_decor.get_rect()
        self.tree_decor_rect.x , self.tree_decor_rect.y = (x,y)
        
    
    def move_decors(self,screen_height):
        self.tree_decor_rect.y += 3
        if self.tree_decor_rect.y > screen_height:
            self.tree_decor_rect.y = -self.tree_decor_rect.height


    def draw_decors(self,screen):
        screen.blit(self.tree_decor,self.tree_decor_rect)

road_side_1_obj =Road_side(5,0)
road_side_2_obj =Road_side(5,430)

road_side_3_obj =Road_side(515,215)
road_side_4_obj =Road_side(515,655)


def draw_all_decor_obj(screen,screen_height):

    road_side_1_obj.draw_decors(screen)
    road_side_1_obj.move_decors(screen_height)

    road_side_2_obj.draw_decors(screen)
    road_side_2_obj.move_decors(screen_height)

    road_side_3_obj.draw_decors(screen)
    road_side_3_obj.move_decors(screen_height)

    road_side_4_obj.draw_decors(screen)
    road_side_4_obj.move_decors(screen_height)