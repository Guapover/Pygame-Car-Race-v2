import pygame
import random
from itertools import combinations

vehicles_imgs = [pygame.image.load("assets/img/c"+str(i)+".png")for i in range(1, 7)]

vehicle_number = random.choice([1,1,1,1,2])

road_coordinates = (130,265,400)

class Vehicles:
    def __init__(self):
        self.vehicle = random.choice(vehicles_imgs)
        self.vehicle_rect = self.vehicle.get_rect()
        self.vehicle_rect.x = random.choice([130,265,400])
        self.vehicle_speed = random.choice([7,8,9,10])



    def move_vehicle(self):
        self.vehicle_rect.y += self.vehicle_speed
    
    def draw_vehicle(self,screen):
        screen.blit(self.vehicle,self.vehicle_rect)
    
    def return_vehicle_rect(self):
        return self.vehicle_rect
    

    def reset_values(self):
        self.vehicle = random.choice(vehicles_imgs)
        self.vehicle_rect.x = random.choice(road_coordinates)
        self.vehicle_rect.y= -self.vehicle_rect.height
    
    def place_vehicles(self,lane):
        self.vehicle = random.choice(vehicles_imgs)
        self.vehicle_rect.x = lane
        self.vehicle_rect.y = -self.vehicle_rect.height
        self.vehicle_speed = random.choice([7,8,9,10])

vehicles_list = []
vehicles_rect_list = []
for i in range(2):
    vehicles_list.append(Vehicles())

for _ in vehicles_list:
    vehicles_rect_list.append(_.vehicle_rect)



def select_vehicle(score_obj):
        global vehicle_number, score ,vehicles_list
        if vehicle_number == 1:
            if vehicles_list[0].vehicle_rect.y > 700:
                vehicle_number = random.choice([1,1,2])
                score_obj.increase_score()

                x1,x2 = random.choice(list(combinations((130,265,400),2)))
                vehicles_list[0].place_vehicles(x1)
                vehicles_list[1].place_vehicles(x2)


        else:
            counter = 0
            for vehicle in vehicles_list:
                if vehicle.vehicle_rect.y > 700:
                    counter +=1
            if counter == vehicle_number:
                vehicle_number = random.choice([1,1,2])
                score_obj.increase_score()
                x1,x2 = random.choice(list(combinations((130,265,400),2)))
                vehicles_list[0].place_vehicles(x1)
                vehicles_list[1].place_vehicles(x2)


def create_vehicles(screen,score_obj):
    global vehicle_number
        
    if vehicle_number == 1:
        create_vehicle(screen,0)
    else:
        create_vehicle(screen,0)
        create_vehicle(screen,1)

    select_vehicle(score_obj)
        
def vehicle_number_return():
    return vehicle_number


def create_vehicle(screen,intex):
    vehicles_list[intex].move_vehicle()
    vehicles_list[intex].draw_vehicle(screen)
    
    
