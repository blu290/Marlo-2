import time
import button
import sys
import math
import random
import player
import copy
import os
try:
    import pygame
    #from pygame.locals import*
except ModuleNotFoundError:
    print("pygame library not found. in order to play this game pygame is required.\nfor more information on how to get pygame, visit https://pypi.org/project/pygame/ \n ")
    print("exiting in 10 seconds...")
    time.sleep(10)
    sys.exit()

#from playsound import playsound
#from sys import platform
#import numpy

#####LEVELGRID AND PROCEDURAL GENERATION#####
def buildGrid():
    gameGrid =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return gameGrid

def walker(grid):
    x = 29
    y = 29
    placed = 0
    whatDir = random.randint(1,4)
    while placed <= 400:
        changeDir = random.randint(1,2)
        if changeDir == 2:
            whatDir = random.randint(1,4)
        
        if whatDir ==1:
            if x < 58:
                x += 1
                placed+= 1
            
        if whatDir ==2:
            if x > 1:
                x -= 1
                placed+= 1
        if whatDir ==3:
            if y < 58:
                y += 1
                placed += 1
            
        if whatDir ==4:
            if y > 1:
                y -= 1
                placed += 1
        grid[y][x] = 1

    return grid

def placeWalls(grid):
    for y in range(60):
        for x in range(60):
            if grid[y][x] == 1:
                
                if y != 60:
                    if grid[y+1][x] == 0:
                        grid[y+1][x] = 2
                        
                if y != 0:
                    if grid[y-1][x] ==0:
                       grid[y-1][x] = 2

                if x != 60:
                    if grid[y][x+1]==0:
                       grid[y][x+1] = 2

                if x != 0:
                    if grid[y][x-1] ==0:
                        grid[y][x-1] = 2
    return(grid)



#initialise the pygame module
pygame.init()
pygame.mixer.pre_init()
pygame.font.init()
#loading the icon file
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
#setting up text font to be used and size:
menuFont = pygame.font.SysFont("comic sans MS",30)

mainMenuText = menuFont.render("main menu",False,(255,255,255))
optionsMenuText = menuFont.render("options",False,(255,255,255))
characterSelectText = menuFont.render("choose your character",False,(255,255,255))
statsText = menuFont.render("stats",False,(255,255,255))


#text for stats stuff:

#these are placeholders to show that it works, in a future version this values will be read from a config file.
highScore = 500
playTime = "60 hours"
mostPlayed = "example"


highScoreText = menuFont.render("high score: {}".format(highScore),False,(255,255,255))
playTimeText = menuFont.render("play time: {}".format(playTime),False,(255,255,255))
mostPlayedText = menuFont.render("most played character: {}".format(mostPlayed),False,(255,255,255))
highScoreTextPos = highScoreText.get_rect()
playTimeTextPos = playTimeText.get_rect()
mostPlayedTextPos = mostPlayedText.get_rect()

#positions for them


mainMenuTextPos = mainMenuText.get_rect()
optionsMenuTextPos = optionsMenuText.get_rect()
characterSelectTextPos = characterSelectText.get_rect()
statsTextPos = statsText.get_rect()

#define the width and height of the window
displayWidth = 800
displayHeight = 600

#variable for the framerate object
clock = pygame.time.Clock()

#draw the screen + change the caption
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight),pygame.RESIZABLE)
pygame.display.set_caption("Marlo 2")
backgroundImage = pygame.image.load("bg.jpg").convert()

#creating play button object
playButtonImage = pygame.image.load("buttons/PlayButton.png").convert()
playButton = button.Button(20,200,playButtonImage,0.25)
play2 = button.Button(20,200,playButtonImage,0.25)

#creating exit button object
exitButtonImage = pygame.image.load("buttons/ExitButton.png").convert()
exitButton = button.Button(20,500,exitButtonImage,0.25)

#creating stats button object
statsButtonImg = pygame.image.load("buttons/Stats.png").convert()
statsButton = button.Button(20,300,statsButtonImg,0.25)

#creating options button
optionsButtonImg = pygame.image.load("buttons/Options.png").convert()
optionsButton = button.Button(20,400,optionsButtonImg,0.25)

#go back (for the select character menu
goBackButtonImg = pygame.image.load("buttons/goBack.png").convert()
goBackButton = button.Button(20,300,goBackButtonImg,0.25)

#same but for options and stats (they will do the same thing and be in same place so the same object can be used)
goBackButtonImg = pygame.image.load("buttons/goBack.png").convert()
goBackButton2 = button.Button(20,500,goBackButtonImg,0.25)

#play button menu objects:
#characters and difficulty buttons
c2Img = pygame.image.load("buttons/Bogos.png").convert()
c1Img = pygame.image.load("buttons/Marlo.png").convert()
character2Button = button.Button(200,500,c2Img,0.25)
character1Button = button.Button(10,500,c1Img,0.25)


easy = pygame.image.load("buttons/Easy.png").convert()
easyButton = button.Button(600,200,easy,0.25)
hard = pygame.image.load("buttons/Hard.png").convert()
hardButton = button.Button(600,300,hard,0.25)

#textures for the tiles
wall = pygame.image.load("textures/TestWall.png").convert()
floor = pygame.image.load("textures/TestFloor.png").convert()

#character image
character1 = pygame.image.load("sprites/tooCool.png").convert()
character2 = pygame.image.load("sprites/Character2.png").convert()
character1.set_colorkey((255,255,255))
character2.set_colorkey((255,255,255))

#loading item pickup images
healthImage = pygame.image.load("sprites/life.png").convert()
healthImage.set_colorkey((255,255,255))

#ghosts sprite
ghostImage = pygame.image.load("sprites/ghost.png").convert()
ghostImage.set_colorkey((255,255,255))

##### MENU functions #####
whatMenu = int(0)

#function for the main menu:
def mainMenu():
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(mainMenuText,(340,0))
    whatMenu = 0
    if optionsButton.draw(gameDisplay) == True:
        whatMenu = int(3)
        
    if statsButton.draw(gameDisplay)==True:
        whatMenu = int(2)
        
    if playButton.draw(gameDisplay) == True:
        whatMenu = int(1)

    if exitButton.draw(gameDisplay) == True:
        pygame.quit()
        sys.exit()
    return whatMenu

#options menu
def optionsMenu():
    whatMenu = 3
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(optionsMenuText,(340,0))
    if goBackButton2.draw(gameDisplay) == True:
        whatMenu = 0
    return whatMenu

#stats menu
def statsMenu():
    whatMenu = 2
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(statsText,(340,0))
    gameDisplay.blit(highScoreText,(20,200))
    gameDisplay.blit(playTimeText,(20,300))
    gameDisplay.blit(mostPlayedText,(20,400))
    if goBackButton2.draw(gameDisplay) == True:
        whatMenu = 0
        
    return whatMenu

#play menu
character = 0
difficulty = 0

#whatMenu is already known and doesn't change until the player hits a button so this doesn't need to be passed
#character and difficulty must be passed


def playMenu(character,difficulty):
    whatMenu = int(1)
    
    #draw background and text    
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(characterSelectText,(280,0))

    #go back button
    if goBackButton.draw(gameDisplay) ==True:
        whatMenu= int(0)
        
    #button for playing    
    if play2.draw(gameDisplay) == True:
        if character != 0 and difficulty != 0:
            whatMenu = 4
            
    #characters and difficulty       
    if character1Button.draw(gameDisplay) == True:
        #print("character 1 selected")
        character = player.Marlo(character1,1,200,150,8,3)

    if character2Button.draw(gameDisplay) == True:
        #print("character 2 selected")
        character = player.Bogos(character2,1,200,150,1,12)

    if hardButton.draw(gameDisplay) == True:
        #print("hard selected")
        difficulty = 2
    if easyButton.draw(gameDisplay) == True:
        #print("easy selected")
        difficulty = 1

    #returns a tuple for character state, difficulty state and where in the menu the player is.
    return (whatMenu,character,difficulty)

#main menu loop
def Menu():
    whatMenu =0
    menuLoop = 1
    while menuLoop == 1:

    #listens for close clicked 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if whatMenu == 0:
            whatMenu = mainMenu()
            character = 0
            difficulty = 0
        
        if whatMenu == 1:
            playMenuTuple = playMenu(character,difficulty)
            whatMenu = playMenuTuple[0]
            character = playMenuTuple[1]
            difficulty = playMenuTuple[2]
        
        
        if whatMenu == 2:
            whatMenu = statsMenu()

        if whatMenu == 3:
            whatMenu = optionsMenu()
        if whatMenu == 4:
            break
#set clockspeed to 60fps and update screen
        pygame.display.update()
        clock.tick(60)
    return (1,character,difficulty)

#function for checking if the player is hitting wall:
def collideTest(rect,tiles):
    collisions = []
    for tile in tiles:
        if tile.colliderect(rect):
            collisions.append(tile)
    return collisions

#handles the bullet collisions with the wall tiles, for each bullet which has been fired.
def bulletCollide(bullets,tiles,cameraOffset):
        collisions = []
    #having a weird bug which happens when it intercepts 2 tiles at once 
    # it deletes the entry twice which isn't good
    # for now putting it in a try except stops the program from crashing but this needs to be fixed later
    #try:
        for bullet in bullets[:]:
                collisionCount = 0
                bullet.update(cameraOffset)
                for tile in tiles:
                    if bullet.rect.colliderect(tile):
                        if collisionCount == 0:
                            collisions.append(bullet)
                            collisionCount += 1
        for bullet in collisions:
            bullets.remove(bullet)
    #except:
       # return 0

def bulletEnemy(bullets,enemyList):
    collisions = []
    for bullet in bullets[:]:                           #loop through all lists
        collisionCount = 0
        for enemy in enemyList:
            if bullet.rect.colliderect(enemy):          #check every possible collision
                if collisionCount == 0:
                    collisions.append(bullet)           #add the bullet to the list if it's collided
                    collisionCount += 1

                if enemy.takeDamage(bullet.getDamage()):#run the method on the enemy to take damage
                    enemyList.remove(enemy)             #if it's true the enemy died, so it is removed from the list

    for bullet in collisions:                           #remove all collided bullets
        bullet.takeDamage()
        if bullet.getHealth() == 0:
            bullets.remove(bullet)

#handles the movement of the player and camera when 
def move(rect, movement, tiles):
    hit_list = collideTest(rect,tiles)
    for tile in hit_list:
        if (rect.right - tile.left) < 4:
            movement[0] += (tile.left - rect.right)
             #these are the same for collisions on that side, perhaps use this to decide where to move the player.
        elif (tile.right - rect.left)<4:
            movement[0] += (tile.right - rect.left)

        elif (rect.bottom -tile.top) <4:
            movement[1] += (tile.top - rect.bottom)

        elif (tile.bottom - rect.top) < 4:
            movement[1] -= (rect.top - tile.bottom)
            
    return movement[0],movement[1]

def enemyWallCollide(rect, movement, tiles):
    hit_list = collideTest(rect,tiles)
    for tile in hit_list:
        if (rect.right - tile.left) < 4:
            movement[0] += (tile.left - rect.right)
             #these are the same for collisions on that side, perhaps use this to decide where to move the player.
        elif (tile.right - rect.left)<4:
            movement[0] += (tile.right - rect.left)

        elif (rect.bottom -tile.top) <4:
            movement[1] += (tile.top - rect.bottom)

        elif (tile.bottom - rect.top) < 4:
            movement[1] -= (rect.top - tile.bottom)
            
    return movement[0],movement[1]

def playerHit(character,enemyList):
    for enemy in enemyList:
        if character.rect.colliderect(enemy):
            if character.takeDamage(enemy.damage) ==1:
                pygame.mixer.Sound("sounds/damage.mp3").play()

def abilityPickup(character,lifeList):                    
    if character.fullSpecial():                             #check if max special
        return 0
    else:
        for life in lifeList:                               #loop through the list of ability pickups
            if character.rect.colliderect(life):            #if colliding
                character.increaseSpecial(life.getHeal())   #increase character's special + kill the pickup
                #character.heal(life.getHeal())
                lifeList.remove(life)                       #remove from the list

def upgradePickup(character,upgradelist):
    for upgrade in upgradelist:
        if character.rect.colliderect(upgrade):
            upgradeType = upgrade.getType()
            if upgradeType == 1:
                character.increaseMaxHealth()
            elif upgradeType == 2:
                character.increaseFireRate()
            elif upgradeType == 3:
                character.increaseDamage()
            elif upgradeType == 4:
                character.increaseMaxSpecial()
            upgradelist.remove(upgrade)

def doorLocation(grid):
    notPicked = True
    while notPicked is True:
        #generate random index for x and y
        x = random.randint(0,(len(grid)-2))
        y = random.randint(0,(len(grid)-2))

        #2 corresponds to a Wall tile
        #if a wall tile is picked out then replace it with a door tile
        if grid[y][x] ==2:
            grid[y][x]= 3
            #exit the loop 
            notPicked = False
            
def findFloors(gameMap):
    floorList = [] #a list that stores a tuple for each location of floor tile, index 0 is x and index y is 1
    for x in range(0,len(gameMap)-1): #loop through each tile
        for y in range(0,len(gameMap)-1):
            if gameMap[y][x] == 1: #if the tile is a floordd
                floorCoordinates = (y,x)
                floorList.append(floorCoordinates)
    return floorList

def shootSound():
    pygame.mixer.Sound("sounds/gun"+str(random.randint(0,4))+".mp3").play()

def placeAngryDudes(gameMap,image,scale,difficulty,howMany):
    floors = findFloors(gameMap)
    #if more enemies than floor tiles then equate them
    if howMany > len(floors)-1:
        howMany = (len(floors) -1)
    enemyList = []
    for i in range(howMany):#len(floors)-1):
        floor = random.randint(0,len(floors)-1) #pick a random index24
        coordinates = floors[floor] #coordinates of the floor tile
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        enemy =  player.angrydude(image,scale,difficulty,x,y,gameMap,i,howMany)
        enemyList.append(enemy)
    return (enemyList)

def placeGhosts(gameMap,image,scale,difficulty,howMany,enemyList):
    floors = findFloors(gameMap)
    #if more enemies than floor tiles then equate them
    if howMany > len(floors)-1:
        howMany = (len(floors) -1)
    for i in range(howMany):#len(floors)-1):
        floor = random.randint(0,len(floors)-1) #pick a random index24
        coordinates = floors[floor] #coordinates of the floor tile
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        enemy =  player.Ghost(image,scale,difficulty,x,y,gameMap,i,howMany)
        enemyList.append(enemy)
    return (enemyList)

def placeLife(gameMap,image,scale,howMany):
    floors = findFloors(gameMap)
    if howMany > len(floors) - 1:
        howMany = len(floors) - 1
    lifeList = []
    for i in range(howMany):
        floor = random.randint(0,len(floors)-1)
        coordinates = floors[floor]
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        life = player.life(image,scale,x,y)
        lifeList.append(life)
    return lifeList

def placeUpgradeBoxes(gameMap,image,scale,howMany):
    floors = findFloors(gameMap)
    if howMany > len(floors) - 1:
        howMany = len(floors) - 1
    upgradeBoxList = []
    for i in range(howMany):
        floor = random.randint(0,len(floors)-1)
        coordinates = floors[floor]
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        upgrade = player.upgrade(image,scale,x,y)
        upgradeBoxList.append(upgrade)

    return (upgradeBoxList)

def createMatrix(gameMap):
    matrix = gameMap
    for y in range(len(matrix)-1):      #loop through the grid
        for x in range(len(matrix)-1):
            if matrix[y][x] != 1:       #if it's not a floor tile
                matrix[y][x] = 0        #make it an obsticle. 
    return matrix

def placePlayer(floors,resolution):
    cameraOffset = [0,0]
    floor = floors[random.randint(0,len(floors)-1)]
    cameraOffset[1] = 32*floor[0] +8 - resolution[1]/4
    cameraOffset[0] = 32*floor[1] +8 - resolution[0]/4
    return cameraOffset


def game(gameMap,character,difficulty,room):
    enemyConstant = 5
    currentRes = gameDisplay.get_size()
    previousRes = currentRes

    floors = findFloors(gameMap)

    #variable which gets returned
    room += 1
    #setting up text for the HUD
    pygame.font.init()
    gameFont = pygame.font.SysFont("arial",15)

    #sprite group for the character, this is needed for the character to be drawn on screen.
    characterSpriteGroup = pygame.sprite.Group()
    characterSpriteGroup.add(character)

    #loading door and game textures 
    door = pygame.image.load("textures/door.png").convert()
    angrydudeimg = pygame.image.load("sprites/angry.png").convert()
    angrydudeimg.set_colorkey((255,255,255))

    #setting up the character's gun sprite:

    pistolImg = pygame.image.load("sprites/pistol.png").convert()
    pistolImg.set_colorkey((255,255,255))


    #setting up some variables required for the game
    tileWidth = 32
    cameraOffset = placePlayer(floors,currentRes)
    #cameraOffset = [24*tileWidth,26*tileWidth]
    gameLoop = 1

    #adding a door to the game
    doorLocation(gameMap)

    #create a list for the hitbox for walls, as well as bullets. declare the shootdelay to be 20 which allows the gun to be instantly fired. 
    tilesRects = []
    bullets = []
    shootDelay = 20

    #setting the player's invincibility frames to 0, when it's 30 or above they can take damage
    gunSpriteGroup = pygame.sprite.Group()
    gun = player.gun(400,300,pistolImg,1,0,cameraOffset)
    gunSpriteGroup.add(gun)

    #AngryDudes being placed and added to the srite group
    enemySpriteGroup = pygame.sprite.Group()
    enemyList = placeAngryDudes(gameMap,angrydudeimg,1,difficulty,enemyConstant*(room-1))
    enemyList = placeGhosts(gameMap,ghostImage,1,difficulty,random.randint(0,room),enemyList)
    for i in range(len(enemyList)):
        enemySpriteGroup.add(enemyList[i])

    #placing life tings
    lifeSpriteGroup = pygame.sprite.Group()
    if difficulty ==2:
        howMany = 1
    else:
        howMany = 2
    lifeList = placeLife(gameMap,healthImage,1,howMany)

    for life in lifeList:
        lifeSpriteGroup.add(life)

    #place the upgrade boxes
    upgradeImage = pygame.image.load("sprites/upgrade.png").convert()
    upgradeImage.set_colorkey((255,255,255))
    upgradeBoxList = placeUpgradeBoxes(gameMap,upgradeImage,1,1)
    upgradeSpriteGroup = pygame.sprite.Group()
    for upgrade in upgradeBoxList:
        upgradeSpriteGroup.add(upgrade)

    #generate the matrix for the map, used for pathfinding
    gameMap2 = copy.deepcopy(gameMap)
    matrix = createMatrix(gameMap2)

    distanceFromDoor = (0,0)
    if os.path.isfile("SUPERMARLO"):
        character.SUPERMARLO()

    character.newLevel()

    #GAME LOOP
    while gameLoop == 1:
        #display scaling things
        screenSizeX,screenSizeY = gameDisplay.get_size()

        currentRes = gameDisplay.get_size()                 #get the current size of the window
        changeInX = currentRes[0] - previousRes[0]          #calculate the change in x and y from the previous res to this res
        changeInY = currentRes[1] - previousRes[1]
        cameraOffset[0] -= changeInX/4                      #change the camera offset accordingly to prevent the player moving
        cameraOffset[1] -= changeInY/4
        previousRes = currentRes
        character.updateScreenPosition(screenSizeX/4,screenSizeY/4)

        display = pygame.Surface((screenSizeX/2,screenSizeY/2))


        healthText = gameFont.render("HP: {} / {}".format(character.health,character.maxHealth),False,(255,255,255))
        roomNumberText = gameFont.render("room: {}/10".format(room-1),False,(255,255,255))
        enemyText = gameFont.render("enemies: {}".format(len(enemyList)),False,(255,255,255))
        distanceText = gameFont.render("{},{}".format(distanceFromDoor[0],distanceFromDoor[1]),False,(255,255,255))
        specialText = gameFont.render("special: {}/{}".format(character.getSpecial(),character.getMaxSpecial()),False,(255,255,255))
        movement = [0,0]
        gameDisplay.fill((0,0,0))
        display.fill((32,36,78))

        #print(character.getTile(cameraOffset,(screenSizeX,screenSizeY)))
        #for badguy in enemyList:
            #print(badguy.getTile(character,cameraOffset,(screenSizeX,screenSizeY)))


#####  _                   _         
##### (_)                 | |      
#####  _ _ __  _ __  _   _| |_ ___
##### | | '_ \| '_ \| | | | __/ __|  
##### | | | | | |_) | |_| | |_\__ \
##### |_|_| |_| .__/ \__,_|\__|___/
#####         | |                    
#####         |_|              
        character.updateShootFrames()

        mousePressed = pygame.mouse.get_pressed()
        if mousePressed[0]:                                                                         #when the mouse button is pressed
            if character.getShootCooldown()>=character.getShootFrames():                            #if the bullet is ready to be fired
                shootSound()
                bullet = player.Bullet(screenSizeX/2,screenSizeY/2,character.damage,cameraOffset,character.getPen())   #create a bullet object and put it in a list
                bullets.append(bullet)
                character.resetShootDelay()                                                         #reset it so its not ready to fire.
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if mousePressed[2]:
                cameraOffset = character.ability(cameraOffset,currentRes,floors)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            movement[0]-=(3)

        if keys[pygame.K_d]:
            movement[0]+=(3)
    
        if keys[pygame.K_w]:
            movement[1]-=(3)
            
        if keys[pygame.K_s]:
            movement[1]+=(3)
            
        display.fill((0,0,0))

        #temporary, press p to take damage, in order to test that the health system works
        if keys[pygame.K_p]:
            character.takeDamage(1)
#####  _                   _                        _ 
##### (_)                 | |                      | |
#####  _ _ __  _ __  _   _| |_ ___    ___ _ __   __| |
##### | | '_ \| '_ \| | | | __/ __|  / _ \ '_ \ / _` |
##### | | | | | |_) | |_| | |_\__ \ |  __/ | | | (_| |
##### |_|_| |_| .__/ \__,_|\__|___/  \___|_| |_|\__,_|
#####         | |                                     
#####         |_| 
        #enemy logic and stuff
        enemyCount = len(enemyList)

        #gun rotation and updating position and such
        gun.update(screenSizeX/4,screenSizeY/4,pistolImg,1)

        #draw the tiles onto the surface
        for y in range(60):
            for x in range(60):
                #draw floors
                if gameMap[y][x] ==1:
                    display.blit(floor,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                #draw walls
                if gameMap[y][x] ==2:    
                    display.blit(wall,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                    tilesRects.append(pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))
                #draw door
                if gameMap[y][x] ==3:
                    doorX,doorY = x,y
                    display.blit(door,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                    doorHitbox = (pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))
                    if enemyCount:
                        tilesRects.append(pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))

        distanceFromDoor = (-doorX*32 + cameraOffset[0]+screenSizeX/4 ,doorY*32-cameraOffset[1]-screenSizeY/4)
        #put the enemy in the correct place

        #for enemy in enemyList:
            #enemy.updatePosition(cameraOffset,(enemy.chasePlayer(character)))
        
        #putting items in the correct places:
        for life in lifeList:
            life.updatePosition(cameraOffset)

        for upgrade in upgradeBoxList:
            upgrade.updatePosition(cameraOffset)

        #bullet interactions and logic in main loop
        bulletCollide(bullets,tilesRects,cameraOffset)
        bulletEnemy(bullets,enemyList)
        playerHit(character,enemyList)
        abilityPickup(character,lifeList)
        upgradePickup(character,upgradeBoxList)

        #pathfinding
        for badguy in enemyList:
            if badguy.getType() == "angrydude":
                badguy.updateTicks()
                badguy.pathfind(character.getTile(cameraOffset,(screenSizeX,screenSizeY)),matrix,badguy.getTile(character,cameraOffset,(screenSizeX,screenSizeY)))
                if badguy.updatePath() == 0:
                    badguy.updatePosition(cameraOffset,(badguy.chasePlayer(character)))
                elif badguy.updatePath() == 1:
                    badguy.updatePosition(cameraOffset,(badguy.movex,badguy.movey))

            elif badguy.getType() == "ghost":
                badguy.updatePosition(cameraOffset,(badguy.chasePlayer(character)))

        #
        for bullet in bullets:
            bullet.draw(display,cameraOffset)
        
        #drawing the HUD text onto the screen
        display.blit(healthText,(0,0))
        display.blit(roomNumberText,(0,15))
        display.blit(enemyText,(screenSizeX/2 - 100 ,0))
        display.blit(distanceText, (screenSizeX/2 - 100,15))
        display.blit(specialText,(0,30))
        
        movement[0],movement[1] = move(character.rect,movement,tilesRects)
        cameraOffset[0] +=movement[0]
        cameraOffset[1] += movement[1]

        #drawing sprite groups            
        #characterSpriteGroup.update()
        characterSpriteGroup.draw(display)
        enemySpriteGroup.draw(display)
        lifeSpriteGroup.draw(display)
        upgradeSpriteGroup.draw(display)
        #gunSpriteGroup.draw(display)
        character.increment()
#break loop conditions
        #collisions between the door and player when the door is unlocked:
        if doorHitbox.colliderect(character.rect) and enemyCount == 0:
            break
        if character.health <= 0:
            break
#break loop condition end

        surf = pygame.transform.scale(display,(screenSizeX,screenSizeY))
        tilesRects = []
        gameDisplay.blit(surf,(0,0))
        pygame.display.update()
        character.invincibilityFrames += 1
        clock.tick(60)
    #terminate all health that hasn't been used by the player
    for life in lifeList:
        life.kill()
    #return the room number if they survive
    if character.health > 0:
        return room
    #return 99 if they died.
    else:
        return 99


def levelGeneration(Array):
    grid = Array
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = placeWalls(grid)

    return grid

gameOrMenu = 0
done = False
while True:
    #if you're in the menu this functions are ran.
    if gameOrMenu == 0:
        returnTuple = Menu()
        gameOrMenu = returnTuple[0]
        character = returnTuple[1]
        difficulty = returnTuple[2]
    
    #the functions below are for the game itself.
    #if the game is won
    if gameOrMenu == 11:
        gameOrMenu = 0
        print("you win!")
        pygame.mixer.Sound("sounds/win.mp3").play()
    #if the character's health drops to 0 or below
    if gameOrMenu ==99:
        gameOrMenu = 0
        print("you died :(")
        pygame.mixer.Sound("sounds/lose.mp3").play()

    #done is always False as nothing changes it
    # every time a room number is returned, this code is ran in order to generate a new grid.     
    if gameOrMenu >= 1 and done == False:
        gameGrid = buildGrid()
        gameMap = levelGeneration(gameGrid)
        gameDisplay.fill((0,0,0))
    #running the game itself. 
    if gameOrMenu >=1:
        gameOrMenu = game(gameMap,character,difficulty,gameOrMenu)

pygame.quit()
sys.exit()