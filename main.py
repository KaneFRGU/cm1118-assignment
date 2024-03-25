# Importing pygame module

import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

jumping = False

ygravity = 0.5
jumpheight = 7
yvelocity = jumpheight

xpos = 100
ypos = 480
run = True

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

    
    

    cube = pygame.draw.rect(window, black, [xpos, ypos, 20, 20])


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keyspressed = pygame.key.get_pressed()

    if keyspressed[pygame.K_w]:
            jumping = True

    if keyspressed[pygame.K_d]:
         xpos += 5

    if keyspressed[pygame.K_a]:
         xpos -= 5


    if jumping:
        ypos -= yvelocity
        yvelocity -= ygravity
        if yvelocity < -jumpheight:
            jumping = False
            yvelocity = jumpheight
            
    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(60)
