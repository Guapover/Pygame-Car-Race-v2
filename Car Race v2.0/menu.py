import pygame


bg = (100, 100, 220)
white = (222, 222, 222)
black = (0, 0, 0)


first_menu_pass = False
run_draw_menu = True
running = True
pause_game = False

class Menu:
    def __init__(self) -> None:
        self.font_logo = pygame.font.SysFont('consolas', 110)
        self.font_button = pygame.font.SysFont('consolas', 80)

        self.play_button = pygame.Rect(205, 300, 190, 80)
        self.quit_button = pygame.Rect(205, 450, 190, 80)

        self.pause_button = pygame.Rect(130, 300, 350, 80)

        #self.select_car_button_car = pygame.Rect()

        self.text_logo = self.font_logo.render("CAR RACE", True,(50,50,130))

    def draw_logo(self, screen):
        screen.fill(bg)
        screen.blit(self.text_logo, (80, 80))

    def first_menu_draw(self, screen):
        global running, first_menu_pass, run_draw_menu
        first_menu_pass = False
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_draw_menu = False
                running = False

            mouse_pos = pygame.mouse.get_pos()

            if pygame.Rect.collidepoint(self.play_button, mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), self.play_button)
                play_button_text = self.font_button.render("PLAY", True, bg)
                if event.type == pygame.MOUSEBUTTONDOWN:

                    run_draw_menu = False

                    first_menu_pass = True
                    screen.fill(bg)
            else:
                pygame.draw.rect(screen, bg, self.play_button)
                play_button_text = self.font_button.render("PLAY", True, white)

            if pygame.Rect.collidepoint(self.quit_button, mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), self.quit_button)
                quit_button_text = self.font_button.render("QUIT", True, bg)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run_draw_menu = False
                    running = False


            else:
                pygame.draw.rect(screen, bg, self.quit_button)
                quit_button_text = self.font_button.render("QUIT", True, white)

            screen.blit(play_button_text, (205, 300))
            screen.blit(quit_button_text, (205, 450))
            pygame.display.update()
    
    def select_vehicle_menu():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_draw_menu = False
                running = False

            mouse_pos = pygame.mouse.get_pos()


    def return_values(self):
        global running,run_draw_menu,first_menu_pass
        menu_values = [running,run_draw_menu,first_menu_pass]
        return menu_values

    def reset_values(self):
        global first_menu_pass,run_draw_menu
        first_menu_pass = False
        run_draw_menu = True
        
    def return_running(self):
        return running





    def pause_game_func(self,screen,pause_game):
        global running
        
        while pause_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pause_game = False

                mouse_pos = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(self.pause_button, mouse_pos):
                    continue_button_text = self.font_button.render("Continue", True, bg)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pause_game = False
                        
                        
                else:
                    continue_button_text = self.font_button.render("Continue", True,white)

                if pygame.Rect.collidepoint(self.quit_button, mouse_pos):
                    quit_button_text = self.font_button.render("QUIT", True, bg)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        running = False
                        pause_game = False

                else:
                    quit_button_text = self.font_button.render("QUIT", True, white)
                
                screen.blit(self.font_button.render("GAME PAUSED", True, (50,50,150)), (50, 100))
                screen.blit(continue_button_text, (130, 300))
                screen.blit(quit_button_text, (205, 450))
                pygame.display.update()


    def return_pause_game(self):
        return pause_game
