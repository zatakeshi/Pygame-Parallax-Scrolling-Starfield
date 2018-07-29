"""

 Scrolling Parallax Starfield by ZaTakeshi
   - Based on Parallax Starfield Simulation by Leonel Machava

 LEFT arrow and RIGHT arrow control starfield movement.
 
"""

import pygame
from random import randint, choice

#Initialise and system vars
pygame.init()
clock = pygame.time.Clock()
SCREENWIDTH = 640
SCREENHEIGHT = 480

WHITE = (240, 240, 240)
LIGHTGREY = (140, 140, 140)
DARKGREY = (90, 90, 90)
DARK = (40, 40, 40)
BLACK = (0, 0, 0)

#Starfield
NUMSTARS = 150
starList = []

#Controls
keys = {'left':False, 'right':False}
exitGame = False
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Scrolling Parallax Starfield")

class Star():
    def __init__(self):

        #Starfield generation based on Leonel's idea of speed determining size
        self.speed = choice([1, 2, 3, 4])
        self.colour = WHITE
        self.size = choice([1, 2])
        
        #Some stars begin offscreen to help illusion when scrolling - could be tightened
        self.xPos = randint(-SCREENWIDTH / 2, SCREENWIDTH * 1.5)
        self.yPos = randint(-SCREENHEIGHT, 0)

        if self.speed == 1:
            self.size = choice([3, 4, 5])
            self.colour = DARK
        elif self.speed == 2:
            self.size = choice([3, 4, 5])
            self.colour = DARKGREY
        elif self.speed == 3:
            self.size = choice([2, 3, 4])
            self.colour = LIGHTGREY

        """

        #Original starfield generation based on concept of 'distance' determining speed and brightness

        self.distance = self.brightness = choice([1, 2, 3, 4])
        self.speed = choice([3, 4, 5])
        self.colour = WHITE
        self.size = choice([2, 3, 4, 5])
        self.xPos = randint(-SCREENWIDTH / 2, SCREENWIDTH * 1.5)
        self.yPos = randint(-SCREENHEIGHT, 0)
        
        if self.distance == 2:
            self.speed = choice([1, 2, 3, 4])
            self.size = choice([1, 2, 3])
            self.colour = LIGHTGREY
        elif self.distance == 3:
            self.speed  = choice([2, 3, 4])
            self.size = choice([1, 2, 3])
            self.colour = DARKGREY
        elif self.distance == 4:
            self.speed = choice([1, 2, 3])
            self.size = choice([2, 3, 4])
            self.colour = DARK

        """

    #Move down the screen, then reinit
    def streakDown(self):
        if self.yPos < SCREENHEIGHT:
            self.yPos += self.speed
        else:
            self.__init__()
    
    def moveLeft(self):
        self.xPos += self.speed * .5
        
    def moveRight(self):
        self.xPos -= self.speed * .5

#Populate list of stars
for i in range(NUMSTARS):
    starList.append(Star())

#Main loop
while not exitGame:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exitGame = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys['left'] = True
            if event.key == pygame.K_RIGHT:
                keys['right'] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys['left'] = False
            if event.key == pygame.K_RIGHT:
                keys['right'] = False

    if keys['left']:
        for Star in starList:
            Star.moveLeft()
            
    if keys['right']:
        for Star in starList:
            Star.moveRight()

    for Star in starList:
        Star.streakDown()
        screen.fill(Star.colour, (Star.xPos, Star.yPos, Star.size, Star.size))

    
    pygame.display.flip()
    clock.tick(80)

pygame.quit()
