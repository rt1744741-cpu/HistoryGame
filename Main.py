<<<<<<< HEAD
import random
import pygame
from Button import Button

# initialize pygame 
pygame.init()

# create window
screen = pygame.display.set_mode((1820, 980)) # width, height 

# create Title for window 
pygame.display.set_caption("HistoryLine")

# Set frame rate
clock = pygame.time.Clock()

# create background objects
back_image = pygame.image.load('Images/Untitled.png')

easy_image = pygame.image.load('Images/easy.png').convert()
easy_image = pygame.transform.scale(easy_image, (200, 100))


moderate_image = pygame.image.load('Images/moderate.png').convert()
moderate_image = pygame.transform.scale(moderate_image, (200, 100))



difficult_image = pygame.image.load('Images/difficult.png').convert()
difficult_image = pygame.transform.scale(difficult_image, (200, 100))

# instructions
easy_info_img = pygame.image.load('Images/MQ10.png')

# moderate_info_img = pygame.image.load('')
# difficult_info_img = pygame.image.load('')

yes_image = pygame.image.load('Images/yes.png')
yes_image = pygame.transform.scale(yes_image, (600, 400))

no_image = pygame.image.load('Images/no.png')
no_image = pygame.transform.scale(no_image, (600, 400))

# fonts/texts
font1 = pygame.font.Font('TitleFontFolder/spqri.ttf', 250)
font2 = pygame.font.Font('TitleFontFolder/spqri.ttf', 50)

text1 = font1.render('HistoryLine', False, 'Black')
text2 = font2.render('Press Enter to Play', False, 'Red')
text3 = font2.render('Click On One of The Game Modes Below: ', False, 'Black')
text4 = font2.render('Loading...', False, 'Black')

# buttons       
B1 = Button(screen, easy_image, 920, 200, centered=True)
B2 = Button(screen, moderate_image, 920, 540, centered=True)
B3 = Button(screen, difficult_image, 920, 900, centered=True)
B4 = Button(screen, difficult_image, 920, 900, centered=True)
B5 = Button(screen, difficult_image, 920, 900, centered=True)

yes_button = Button(screen, yes_image, 700, 600, centered=True)
no_button = Button(screen, no_image, 1100, 600, centered=True)

# questions 
Q1 = pygame.image.load('Images/Q1.png')


# designing the game menu
running = True
game_started = False
mode_decided = False
game_mode = None
loading_started = False
loading_start_time = 0
show_questions = False
mode_decided = False
game_mode = None
game_state = "intro"

while running:
    # program we want to run 

    # when to quit displaying info
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # this will end the game loop and quit the game
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               game_started = True
            if event.key == pygame.K_ESCAPE:
                running = False 
            
    # displays game menu - first screen
    if not game_started:
        screen.blit(back_image, (0, 0))
        screen.blit(text1, (50, 200))
        screen.blit(text2, (650, 750))
    
    # designing the game mode page - 2nd screen
    elif game_started and not mode_decided:
        screen.fill("White")
        screen.blit(text3, (330, 0))
        if B1.draw():
            game_mode = "easy" 
            mode_decided = True
        if B2.draw():
            game_mode = "moderate" 
            mode_decided = True
        if B3.draw():
            game_mode = "difficult" 
            mode_decided = True
    
    elif not show_questions and not loading_started:
        loading_started = True
        loading_start_time = pygame.time.get_ticks()
        mode_decided = False

    elif loading_started:
        screen.fill("White") # 3rd screen - loading page for web/app affect , should add 15s timer
        screen.blit(text4, (800, 300))

        # check if 15s has passed
        if pygame.time.get_ticks() - loading_start_time > 5000:
            loading_started = False
            show_questions = True 
    
    elif show_questions:
        screen.fill("White") # new screen: display questions call question class
        
        if game_mode == "easy": 
            
            if game_state == "intro":
                screen.blit(easy_info_img, (415, 100)) 
            
            # create yes and no button - if use hits no return to the game menu
            if no_button.draw():
                game_started = False
                show_questions = False
                game_state = "menu"
                
            elif yes_button.draw():
                game_state = "question_1"
        
        elif game_state == "question_1":
            screen.blit(Q1, (415, 50))
    
    pygame.display.update()
    clock.tick(60)






    # screen.fill('Blue')
    


    # x = input("Press Enter To Play")

    # while x != "":
    #     x = input("Press Enter To Play")

    # print("Game Modes: \nEasy\nModerate\nDifficult")
    # # Easy - 10 questions all mutliple choice
    # # Medium - 10 multiple choice, 5 non-multiple choice
    # # Difficult - 20 non-multiple choice questions

    # gameMode = input("Enter the Game Mode You Want To Play: ")
=======
import random

x = input("Press Enter To Play")

while x != "":
    x = input("Press Enter To Play")

print("Game Modes: \nEasy\nModerate\nDifficult")
# Easy - 10 questions all mutliple choice
# Medium - 10 multiple choice, 5 non-multiple choice
# Difficult - 20 non-multiple choice questions

gameMode = input("Enter the Game Mode You Want To Play: ")

 #if gameMode.casefold() == 
>>>>>>> 8615d5748e8cdeefb8cbcb522c2bace5989234d7
