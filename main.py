# Importing pygame module
import math
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

xpos1 = 50
xpos2 = 400
ypos1 = 300
ypos2 = 480
run = True
gravity = -5


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pi = 3.141592653

# N - Creating text for mouse coordinates                                               
font = pygame.font.SysFont(None, 24)


# N - power bar
class PowerBar(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        self.color = red

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

# N - Creating bullet projectiles 
# ref - https://www.youtube.com/watch?v=_gDOz7E6HVM
class Bullet(object):
    # N - creating a circle where the middle is x and y coordinates
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    # N - updates/draws the bullet - used in redrawFrame 
    def draw(self, window):
        pygame.draw.circle(window, white, (self.x,self.y), self.radius)

    # N - moving x and y depedning on the trajectory fired by the bullet
    @staticmethod
    def bulletTrajectory(startx, starty, speed, time):
        velocityx = math.cos(trajectory) * speed
        velocityy = math.sin(trajectory) * speed 

        # N - calculating the distances depending on the time (speed)
        distanceX = velocityx * time
        distanceY = (velocityy * time) + ((gravity * (time ** 2)) / 2)

        # N - calculating new position (round is not needed but better for program)
        nextx = round(distanceX + startx)
        nexty = round(starty - distanceY)

        return (nextx, nexty)

# N - creating a circle where the middle is x and y coordinates
def findTrajectory(pos):
    radianX = bullet.x
    radianY = bullet.y

    try:
        trajectory = math.atan((radianY - pos[1]) / (radianX - pos[0]))
    except:
        trajectory = math.pi / 2

    # N - finds mouse coordinates and compares them to radians in the circle (refer to image: circle.png)
    if pos[1] < radianY and pos[0] > radianX: # 1
        trajectory = abs(trajectory)
    elif pos[1] < radianY and pos[0] < radianX: # 2
        trajectory = math.pi - trajectory
    elif pos[1] > radianY and pos[0] < radianX: # 3
        trajectory = math.pi + abs(trajectory)
    elif pos[1] > radianY and pos[0] > radianX: # 4
        trajectory = (math.pi * 2) - trajectory

    return trajectory

# N - to redraw frames in the game will probably needd to do something similar with the cubes and terrain cuz its flickering alot now
def redrawFrame():
    window.fill((64,64,64))
    bullet.draw(window)
    powerBar.draw(window)
    pygame.draw.line(window, (0,0,0),line[0], line[1])
    pygame.display.update()

    # N - display mouse coordinates
    mousex = font.render('Mouse (X, Y) = ' + str(pygame.mouse.get_pos()), True, white)
    window.blit(mousex, (20, 20))

# N - making the powerbar
powerBar = PowerBar(20, 40, 80, 10, red)

# N - begining bullet position (move with player cube)
bullet = Bullet(xpos1+20, xpos2-100, 2, white)

# R - This part is to manually define the peaks of the hills. The points are manually generated.
terrain_points = [
    (0, 550), (50, 530), (100, 540), (150, 520),
    (200, 500), (250, 480), (300, 500), (350, 520),
    (400, 500), (450, 480), (500, 500), (550, 520),
    (600, 540)
]

# N - variable setup for bullet
run = True
time = 0
speed = 0
trajectory = 0
shoot = False

# K - for time
clock = pygame.time.Clock()
while run:
    # Fill the scree with white color
    window.fill((255, 255, 255))


       




    if shoot:
        # N - will need to edit the "550" for terrain colison as for now it just goes acts dependant on the y axis
        if bullet.y < 550:
            # N - time controls the speed of the bullet ( change if need )
            time += 0.3
            po = Bullet.bulletTrajectory(x, y, speed, time)
            bullet.x = po[0]
            bullet.y = po[1]
        else:
            shoot = False
            time = 0 # N - sets it still
            bullet.x = xpos1 + 20
            bullet.y = ypos1

    line = [(xpos1 + 20, ypos1), pygame.mouse.get_pos()]
    redrawFrame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                # N - x and y for bulletTrajectory
                x = bullet.x
                y = bullet.y
                pos = pygame.mouse.get_pos()
                shoot = True
                # N - formula of the lenght of the line (because of how fast the projectile would be, divide by a number to lessen the effect of the distance)
                trajectory = findTrajectory(pos)
        #K increaases the trajectory of the bulled when A or D is pressed, with 100 as the limit
        if keyspressed[K_d] and speed < 100:
            speed += 1
        if keyspressed[K_a] and speed > 0:
            speed -= 1
        print(speed)




  # R - Draw hills

    pygame.draw.lines(window, green, False, terrain_points, 5)


 # R - Auto adjust the x and y position of cube to nearest terrain segment
    def adjust_cube_position(xpos, ypos):
        for i in range(len(terrain_points) - 1):
            if terrain_points[i][0] <= xpos <= terrain_points[i + 1][0]:
                # Calculate the slope of the terrain segment (Generative AI-Assisted)
                slope = ((terrain_points[i + 1][1] - terrain_points[i][1]) /
                         (terrain_points[i + 1][0] - terrain_points[i][0]))
                # Calculate the y-intercept of the terrain segment
                y_intercept = terrain_points[i][1] - slope * terrain_points[i][0]
                # Adjust ypos based on the line equation
                ypos = slope * xpos + y_intercept - 20  # Adjust for cube height
                break
        return xpos, ypos

    # R -  Don't touch this or else you can't jump
    if not jumping2:
        xpos2, ypos2 = adjust_cube_position(xpos2, ypos2)

    cube1 = pygame.draw.rect(window, red, [xpos1, ypos1, 20, 20])
    cube2 = pygame.draw.rect(window, blue, [xpos2, ypos2, 20, 20])



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keyspressed = pygame.key.get_pressed()



 #player 2 controls
    if keyspressed[pygame.K_UP]:
        jumping2 = True

    if keyspressed[pygame.K_RIGHT] and xpos2 < 580:
        xpos2 += 5

    if keyspressed[pygame.K_LEFT] and xpos2 > 0:
        xpos2 -= 5


#2 different jumping states for each player 
    if jumping2:
        ypos2 -= yvelocity2
        yvelocity2 -= ygravity2
        if yvelocity2 < -jumpheight2:
            jumping2 = False
            yvelocity2 = jumpheight2
     
    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(60)
