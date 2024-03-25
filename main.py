# Importing pygame module

import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

#2 different variables for 2 players, cant be done if variables are the same
jumping1 = False
jumping2 = False

ygravity1 = 0.5
jumpheight1 = 7
yvelocity1 = jumpheight1

ygravity2 = 0.5
jumpheight2 = 7
yvelocity2 = jumpheight1

xpos1 = 100
xpos2 = 400
ypos1 = 480
ypos2 = 480
run = True

#for time
clock = pygame.time.Clock()
while run:
    # Fill the scree with white color
    window.fill((255, 255, 255))
    
    
    # Define the colors we will use in RGB format
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    pi = 3.141592653
     # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
  
   
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.

    pygame.draw.line(window, green, [0, 500], [600, 500], 5)

    cube1 = pygame.draw.rect(window, red, [xpos1, ypos1, 20, 20])
    cube2 = pygame.draw.rect(window, blue, [xpos2, ypos2, 20, 20])


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keyspressed = pygame.key.get_pressed()

 #player 1 controls
    if keyspressed[pygame.K_w]:
            jumping1 = True

    if keyspressed[pygame.K_d]:
         xpos1 += 5

    if keyspressed[pygame.K_a]:
         xpos1 -= 5

 #player 2 controls
    if keyspressed[pygame.K_UP]:
            jumping2 = True

    if keyspressed[pygame.K_RIGHT]:
         xpos2 += 5

    if keyspressed[pygame.K_LEFT]:
         xpos2 -= 5


#2 different jumping states for each player
    if jumping1:
        ypos1 -= yvelocity1
        yvelocity1 -= ygravity1
        if yvelocity1 < -jumpheight1:
            jumping1 = False
            yvelocity1 = jumpheight1
    
    if jumping2:
        ypos2 -= yvelocity2
        yvelocity2 -= ygravity2
        if yvelocity2 < -jumpheight2:
            jumping2 = False
            yvelocity2 = jumpheight2
     
    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(60)
