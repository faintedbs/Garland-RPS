# file created by Kyle Herbold

# Modified from kyles code

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# libraries
# creates suspence for user as it pauses beofre returning the result
from time import sleep
# random number generater to make the game fair
# random psuedo random
from random import randint


# setup asset folders -imgaes and sounds 
# tells us where we are
game_folder = os.path.dirname(__file__)
print(game_folder)


# game settings
WIDTH = 720
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors")
clock = pg.time.Clock()


rock_image = pg.image.load(os.path.join(game_folder,  "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()


# creates transparency
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)


# gets the geometry of the image
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect.y = HEIGHT/2
scissors_rect.x = WIDTH/2

# choices = [0,1,2]
# choices = ["rock", "paper", "scissors"]

# 5 sec pause
# sleep(1)

# printing the choice of the game for the person to select from
# print("let's play:" + str(choices))
"""print("let's play a game!: rock paper scissors")
print("choose rock paper or scissors")"""


# reading what the player types out
user_choice = pg.MOUSEBUTTONUP
# repeat the choice back to the user
# print("you chose " + user_choice)

choices = ["rock", "paper", "scissors"]
def cpu_choice():
    # cpu choice is a function that returns a random integer and returns  the function choices0
    return choices[randint(0,2)]
    

def compare(user_choice, cpu_choice):
    # cpu now has the value of rock paper and scissors allowing us to compar the use choice tot he cpu
    # cpu = cpu_choice()
    print("the computer chose" , cpu_choice)

 



running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            if event.type ==pg.MOUSEBUTTONDOWN:
                mouse_coords = pg.mouse.get_pos()
            if (rock_rect.collidepoint(mouse_coords)) == True :
                print ("you chose rock")
                user_choice = "rock"
            elif paper_rect.collidepoint(mouse_coords) == True :
                print("you chose paper")
                user_choice = "paper"
            elif scissors_rect.collidepoint(mouse_coords) == True:
                print("you chose scissors")
                user_choice = "scissors"
            else :   
                print("please chose one of the three options")
                

            # if mouse_coords[0] <= 200 and mouse_coords[1] <= 188:
            #     print("your chose rock!")
            # else :
            #     print("welp")

    #  get input from player
def compare(user_choice, cpu):
    cpu_choice == cpu
    if user_choice == cpu:
                    print("tie")
    elif user_choice == "rock" and cpu == "scissors" :
                    print ("WINNER!")  
    elif user_choice == "rock" and cpu == "paper" :
                    print ("LOSE!")  
    elif user_choice == "paper" and cpu == "scissors" :
                    print ("LOSE!")  
    elif user_choice == "paper" and cpu == "rock" :
                    print ("WINNER!")  
    elif user_choice == "scissors" and cpu == "rock" :
                    print ("LOSE!")  
    elif user_choice == "scissors" and cpu == "paper" :
                    print ("WINNER!")  
        # else:
        #     print("user error")

    # update
    # rock_rect.y -= 1
    # paper_rect.y += 1
    # scissors_rect.x += 1
    # scissors_rect.y += 1
    # draw
screen.fill(WHITE)
screen.blit(scissors_image, scissors_rect)
screen.blit(paper_image, paper_rect)
screen.blit(rock_image, rock_rect)


pg.display.flip()
# compare(user_choice, cpu_choice)

pg.quit()




