import pygame
from menu import *
from road import *
from player import *
from vehicles import *
from road_side import *
from score import *


pygame.init()

# Screen
screen_width = 600
screen_height = 700
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Race')

# Colors
white = (222, 222, 222)
black = (0, 0, 0)
red = (200,0,0)
yellow = (180,180,0)
orange = (200,110,0)
blue = (0,0,200)
purple = (100,0,100)
grey = (100,100,100)


# Frame Settings
clock = pygame.time.Clock()
fps = 70

# Functions
def main_menu_draw():
    global running, run_draw_menu, first_menu_pass
    while run_draw_menu:
        if not first_menu_pass:
            menu_class.draw_logo(screen)
            menu_class.first_menu_draw(screen)
        #if not select_vehile_menu_pass:


        # menu return
        values_list = menu_class.return_values()
        running = values_list[0]
        run_draw_menu = values_list[1]
        first_menu_pass = values_list[2]



def game_over():
    global first_menu_pass,run_draw_menu
    if player_class.collide_car(vehicles_rect_list,screen):
        pygame.display.update()
        pygame.time.delay(2000)
        screen.fill(bg)
        first_menu_pass = False
        run_draw_menu = True
        player_class.starting_game =True

        for vehicle in vehicles_list:
            vehicle.reset_values()

        score_obj.game_score = 0

        menu_class.reset_values()

def coin():
    if score_obj.coin(vehicle_number_return()):
        score_obj.coin_create(screen_height,vehicles_list[0].return_vehicle_rect())
        score_obj.coin_draw(screen)
        score_obj.collide_car(player_class.return_player_rect())
        score_obj.collide_vehicle_coin(vehicles_list[0].return_vehicle_rect())



# Classes

menu_class = Menu()
road_class = Road()
player_class = Player()
score_obj = Score()


# Game Loop
running = True
while running:
    
    menu_class.pause_game_func(screen,player_class.return_pause_game())

    main_menu_draw()

    

    road_class.draw_road(screen)
    road_class.draw_lines(screen) 

    player_class.move_player()
    player_class.draw_player(screen)
    

    draw_all_decor_obj(screen,screen_height)
    score_obj.write_score(screen)
    player_class.write_speed(screen,fps)

    create_vehicles(screen,score_obj)
    coin()
    

    game_over()

    running = player_class.return_running()
    running = menu_class.return_running()
    pause_game = menu_class.return_pause_game()
    fps += player_class.return_speed()


    clock.tick(fps)
    pygame.display.update()

pygame.quit()
