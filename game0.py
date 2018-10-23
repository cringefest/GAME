import pygame
import numbers
import random

pygame.init()

screen_width = 785
screen_height = 442

clock = pygame.time.Clock()
white = (255,255,255)
black =(0,0,0)
brown = (139,131,120)


backgroundImg = pygame.image.load('back.jpg')
dragonImg = pygame.image.load('dragon.png')
wizardImg = pygame.image.load('wizard.png')
heartImg = pygame.image.load('heart.png')
blackheartImg = pygame.image.load('blackheart.png')
victoryImg = pygame.image.load('victory.png')
lightningImg = pygame.image.load('lightning.png')
deaddragonImg = pygame.image.load('dragon_dead.png')
fireballImg = pygame.image.load('fireball.png')
defeatImg = pygame.image.load('youdied.png')

def background(x,y):
    screen.blit(backgroundImg,(x,y))

def dragon(x,y):
    screen.blit(dragonImg,(x,y))

def wizard(x,y):
    screen.blit(wizardImg,(x,y))

def heart(x,y):
    screen.blit(heartImg,(x,y))

def blackheart(x,y):
    screen.blit(blackheartImg,(x,y))

def intro_background(x,y):
    screen.blit(intro_backgroundImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def button_text(msg, x, y):
    buttonText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,buttonText)
    textRect.center = ((x+40,y+25))
    screen.blit(textSurf,textRect)

def random_choices(amount, max_number):
    random_choices = []
    type_choices = []
    even = numbers.even_numbers(max_number)
    lucky = numbers.lucky_numbers(max_number)
    ulam = numbers.ulam_numbers(max_number)
    noteven = numbers.not_even(max_number)
    notlucky = numbers.not_lucky(max_number)
    notulam = numbers.not_ulam(max_number)
    for i in range(amount):
        choice = []
        type_choice = random.randrange(3)
        if type_choice == 0:
            type_choices.append(type_choice)
            choice.append(random.choice(even))
            choice.append(random.choice(noteven))
            choice.append(random.choice(noteven))
            while choice[1] == choice[2]:
                choice[2] = random.choice(noteven)
        elif type_choice == 1:
            type_choices.append(type_choice)
            choice.append(random.choice(lucky))
            choice.append(random.choice(notlucky))
            choice.append(random.choice(notlucky))
            while choice[1] == choice[2]:
                choice[2] = random.choice(notlucky)
        else:
            type_choices.append(type_choice)
            choice.append(random.choice(ulam))
            choice.append(random.choice(notulam))
            choice.append(random.choice(notulam))
            while choice[1] == choice[2]:
                choice[2] = random.choice(notulam)
        random.shuffle(choice)
        random_choices.append(choice)
    return (random_choices, type_choices)


screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Wizard's Bizzare Adventure")

screen.fill(white)


def game_start():
    clock.tick(60)


    intro_running = True


    while intro_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_intro.collidepoint(event.pos):
                        game_difficulty()


        background(0,0)
        wizard(250, -100)

        button_intro = pygame.Rect(50, 100, 150, 100)
        button_intro_surface = pygame.Surface((150, 100))
        button_intro_surface.fill(brown)
        screen.blit(button_intro_surface, (50, 100))





        button_text("ПРАВИЛА ГРИ", 370,320)
        button_text("Потрібно серед 3 чисел обрати число вказаного типу", 360,350)
        button_text("START", 80, 120)









        pygame.display.update()












def game_difficulty():
    clock.tick(60)


    intro_running = True


    while intro_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_easy.collidepoint(event.pos):
                        game_loop(25)


                    if button_hard.collidepoint(event.pos):
                        game_loop(50)


        background(0,0)
        wizard(250, -100)

        button_easy = pygame.Rect(550, 100, 150, 100)
        button_easy_surface = pygame.Surface((150, 100))
        button_easy_surface.fill(brown)
        screen.blit(button_easy_surface, (550, 100))

        button_hard = pygame.Rect(550, 250, 150, 100)
        button_hard_surface = pygame.Surface((150, 100))
        button_hard_surface.fill(brown)
        screen.blit(button_hard_surface, (550, 250))




        button_text("EASY", 580,120)
        button_text("HARD", 580,270)
        button_text("CHOOSE THE DIFFICULTY", 130,50)









        pygame.display.update()









def game_loop(max_number):
    clock.tick(60)
    choices = random_choices(11, max_number)
    even = numbers.even_numbers(max_number)
    lucky = numbers.lucky_numbers(max_number)
    ulam = numbers.ulam_numbers(max_number)
    noteven = numbers.not_even(max_number)
    notlucky = numbers.not_lucky(max_number)
    notulam = numbers.not_ulam(max_number)
    # type_choices = []
    # for i in range(12):
    #     type_choices.append(random.randrange(3))
    player_hp = 3
    dragon_hp = 9
    round = 0
    lightning_x1 = lightning_x2 = lightning_x3 = lightning_x4 = lightning_x5 =\
                   lightning_x6 = lightning_x7 = lightning_x8 = lightning_x9 =\
                   250
    lightning_dx = 15
    fireball_x1 = fireball_x2 = fireball_x3 = 400
    fireball_dx = 15
    running = False


    while not running:



        button_restart = pygame.Rect(320, 300, 150, 50)
        button_restart_surface = pygame.Surface((150, 50))
        button_restart_surface.fill(brown)

        button_change_difficulty = pygame.Rect(285, 375, 220, 50)
        button_change_difficulty_surface = pygame.Surface((220, 50))
        button_change_difficulty_surface.fill(brown)




        blackhearts = []
        background(0,0)
        dragon(450,170)
        wizard(80,-50)
        for i in range(200,270,30):
            heart(i,140)
        for j in range(440, 710, 30):
            heart(j,140)

        if round == 0:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))


                # if player_hp == 0 or dragon_hp == 0:
                #     break



                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:

                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1


        if round == 1:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1


        if round == 2:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 3:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 4:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 5:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 6:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 7:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 8:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1


        if round == 9:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))





                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                    round += 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                                    round += 1

        if round == 10:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))




                button_text(str(choices[0][round][0]), 200, 50)
                button_text(str(choices[0][round][1]), 347, 50)
                button_text(str(choices[0][round][2]), 494, 50)

                if choices[1][round] == 0:
                    button_text("even", 345, 0)
                elif choices[1][round] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)





                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if choices[1][round] == 0:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in even)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in even)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in even)):
                                    dragon_hp -= 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                            elif choices[1][round] == 1:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in lucky)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in lucky)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in lucky)):
                                    dragon_hp -= 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1
                            else:
                                if (button1.collidepoint(event.pos) and (choices[0][round][0] in ulam)) or (button2.collidepoint(event.pos) and (choices[0][round][1] in ulam)) or (button3.collidepoint(event.pos) and (choices[0][round][2] in ulam)):
                                    dragon_hp -= 1
                                elif button1.collidepoint(event.pos) or button2.collidepoint(event.pos) or button3.collidepoint(event.pos):
                                    player_hp -= 1

        if round == 11:


                panel_surface = pygame.Surface((120, 40))
                panel_surface.fill(brown)
                screen.blit(panel_surface, (332, 0))

                button1 = pygame.Rect(200, 50, 91, 50)
                button1_surface = pygame.Surface((91, 50))
                button1_surface.fill(brown)
                screen.blit(button1_surface, (200, 50))

                button2 = pygame.Rect(347, 50, 91, 50)
                button2_surface = pygame.Surface((91, 50))
                button2_surface.fill(brown)
                screen.blit(button2_surface, (347, 50))

                button3 = pygame.Rect(494, 50, 91, 50)
                button3_surface = pygame.Surface((91, 50))
                button3_surface.fill(brown)
                screen.blit(button3_surface, (494, 50))




                button_text(str(choices[0][10][0]), 200, 50)
                button_text(str(choices[0][10][1]), 347, 50)
                button_text(str(choices[0][10][2]), 494, 50)

                if choices[1][10] == 0:
                    button_text("even", 345, 0)
                elif choices[1][10] == 1:
                    button_text("lucky", 345, 0)
                else:
                    button_text("ulam", 345, 0)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if button1.collidepoint(event.pos):
                                pass


        else:
            pass










            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         if button1.collidepoint(event.pos):
            #             dragon_hp -= 1

        if dragon_hp <= 8:
            lightning_x1 += lightning_dx
            screen.blit(lightningImg, (lightning_x1, 200))
            blackhearts.append((blackheartImg, (680, 140)))
        if dragon_hp <= 7:
            lightning_x2 += lightning_dx
            screen.blit(lightningImg, (lightning_x2, 200))
            blackhearts.append((blackheartImg, (650, 140)))
        if dragon_hp <= 6:
            lightning_x3 += lightning_dx
            screen.blit(lightningImg, (lightning_x3, 200))
            blackhearts.append((blackheartImg, (620, 140)))
        if dragon_hp <= 5:
            lightning_x4 += lightning_dx
            screen.blit(lightningImg, (lightning_x4, 200))
            blackhearts.append((blackheartImg, (590, 140)))
        if dragon_hp <= 4:
            lightning_x5 += lightning_dx
            screen.blit(lightningImg, (lightning_x5, 200))
            blackhearts.append((blackheartImg, (560, 140)))
        if dragon_hp <= 3:
            lightning_x6 += lightning_dx
            screen.blit(lightningImg, (lightning_x6, 200))
            blackhearts.append((blackheartImg, (530, 140)))
        if dragon_hp <= 2:
            lightning_x7 += lightning_dx
            screen.blit(lightningImg, (lightning_x7, 200))
            blackhearts.append((blackheartImg, (500, 140)))
        if dragon_hp <= 1:
            lightning_x8 += lightning_dx
            screen.blit(lightningImg, (lightning_x8, 200))
            blackhearts.append((blackheartImg, (470, 140)))
        if dragon_hp <= 0:
            blackhearts.append((blackheartImg, (440, 140)))

        if player_hp <=2:
            fireball_x1 -= fireball_dx
            screen.blit(fireballImg, (fireball_x1, 200))
            blackhearts.append((blackheartImg, (260, 140)))
        if player_hp <=1:
            fireball_x2 -= fireball_dx
            screen.blit(fireballImg, (fireball_x2, 200))
            blackhearts.append((blackheartImg, (230, 140)))
        if player_hp <=0:
            blackhearts.append((blackheartImg, (200, 140)))


        for (img, pos) in blackhearts:
            screen.blit(img, pos)

        if dragon_hp <= 0:
            round = 12
            screen.blit(deaddragonImg, (450,170))
            lightning_x9 += lightning_dx
            screen.blit(lightningImg, (lightning_x9, 200))
            screen.blit(victoryImg, (100, -30))

            screen.blit(button_restart_surface, (320, 300))
            button_text("RESTART",350,300)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if button_restart.collidepoint(event.pos):
                            game_loop(max_number)


        if player_hp <= 0:
            round = 12
            fireball_x3 -= fireball_dx
            screen.blit(fireballImg,(fireball_x3,200))
            screen.blit(defeatImg,(0,0))

            screen.blit(button_restart_surface, (320, 300))
            button_text("RESTART",350,300)

            screen.blit(button_change_difficulty_surface, (285, 375))
            button_text("CHANGE DIFFICULTY",350,375)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if button_restart.collidepoint(event.pos):
                            game_loop(max_number)

                        if button_change_difficulty.collidepoint(event.pos):
                            game_difficulty()









        pygame.display.update()




game_start()
pygame.quit()
quit()
