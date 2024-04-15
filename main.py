
# Importing pygame module
import math
import pygame
import random
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

# F - Creates coordinates for the missBar
barposX = 0
barposY = 560

run = True
gravity = -5


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pi = 3.141592653

#L- font used for the scoreboard
font = pygame.font.Font(None,36)

#L- red and blue scores
RedScore = 0
BlueScore = 0


# N - Creating text shooter coordinates                                               
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

    # N - finds shooter coordinates and compares them to radians in the circle (refer to image: circle.png)
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
    
    # N - display shooter coordinates
    shooterPrint = font.render('shooter (X, Y) = ' + str(shooterX) + ', ' + str(shooterY), True, white)
    window.blit(shooterPrint, (20, 20))



# N - begining bullet position (move with player cube)
bullet = Bullet(xpos1+20, xpos2-100, 2, white)

# R - This part is to manually define the plateaus of the hills. The points are manually generated.
terrain_points = [
    (0, 325), (90, 325), (150, 470),
    (200, 470), (250, 520), (300, 520),
    (350, 480), (400, 480), (450, 550),
    (500, 550), (550, 530), (600, 530)
]

# N - variable setup for bullet
run = True
time = 0
speed = 0
trajectory = 0
shoot = False


# N - making the powerbar
powerBar = PowerBar(20, 40, speed, 10, red)

# K - for time
clock = pygame.time.Clock()

# N - wasd x and y positions
shooterX = 0
shooterY = 0
shooterpos = [shooterX, shooterY]


#K power bar color
barR = 0
barG = 255
while run:
    # Fill the scree with white color
    window.fill((255, 255, 255))

    if shoot:
        # N - will need to edit the "550" for terrain colison as for now it just goes acts dependant on the y 
        
        #K increaases the trajectory of the bulled when A or D is pressed, with 100 as the limit
        


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

    line = [(xpos1 + 20, ypos1), [shooterX, shooterY]]
    redrawFrame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keyspressed = pygame.key.get_pressed()

        # N - for SPACE you need to get keydown too or it wont work, if changing key you can remove this
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if not shoot:
                # N - x and y for bulletTrajectory
                x = bullet.x
                y = bullet.y
                pos = [shooterX, shooterY]
                shoot = True
                
                trajectory = findTrajectory(pos)

        if keyspressed[K_e] and speed < 50:
            speed += 1
            barR += 5.1
            barG -= 5.1
        if keyspressed[K_q] and speed > 0:
            speed -= 1
            barR -= 5.1
            barG += 5.1
        
        # N - gets x and y position with wasd
        if keyspressed[K_a]:
            shooterX -= 10
        if keyspressed[K_d]:
            shooterX += 10
        if keyspressed[K_w]:
            shooterY -= 10
        if keyspressed[K_s]:
            shooterY += 10
            




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

 
    #K - initialising power bar
    bar = pygame.draw.rect(window, [barR, barG, 0], [20, 40, speed * 4, 20])



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # F - Creates hitbox for the bullet to allow collision with the player
    hitbox = pygame.draw.rect(window, white, [bullet.x - 2.5, bullet.y - 2.5, 5, 5])

    # F - Creates a bar at the bottom of a window which the bullet will collide with if it misses the player
    missBar = pygame.draw.rect(window, (64, 64, 64), [barposX, barposY, 600, 5])


    # F - Creates collision with bullet and player and makes the player respawn to a random location when hit
    hashit = False

    if cube2.colliderect(hitbox):
        hashit = True
        hit = font.render('Hit!', True, white)
        window.blit(hit, (300, 300))
        xpos2 = random.randint(100, 580)
        pygame.display.update()
        pygame.time.delay(1000)        
        hashit = False
        if hashit == False:
            bullet.x = 70
            bullet.y = 300  
    #L - whenever Red hits Blue a point is given to red and if red reaches 10 red wins and the game restarts
        RedScore += 1
        if RedScore == 10:
            print("Red wins!")
            WinnerMessage = font.render("Red wins!", True, (red))
            window.blit(WinnerMessage, (250,250))
            pygame.display.update()
            pygame.time.delay(5000)
            RedScore = 0
            BlueScore = 0

        
    if hitbox.colliderect(missBar):
        miss = font.render('Miss!', True, white)
        window.blit(miss, (300, 300)) 
        pygame.display.update()
        pygame.time.delay(1000)
    #L - Whenever red misses blue a point is given to blue and if blue reaches 10 blue wins and the game restarts
        BlueScore += 1
        if BlueScore == 10:
            print("Blue wins!")
            WinnerMessage = font.render("Blue wins!", True, (blue))
            window.blit(WinnerMessage, (250,250))
            pygame.display.update()
            pygame.time.delay(5000)
            BlueScore = 0
            RedScore = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

 #player 2 controls
    if keyspressed[pygame.K_UP]:
        jumping2 = True

    if keyspressed[pygame.K_RIGHT]:
        xpos2 += 5

    if keyspressed[pygame.K_LEFT]:
        xpos2 -= 5


#2 different jumping states for each player 
    if jumping2:
        ypos2 -= yvelocity2
        yvelocity2 -= ygravity2
        if yvelocity2 < -jumpheight2:
            jumping2 = False
            yvelocity2 = jumpheight2

 # Scoreboard display
    score_text = font.render(f"Red: {RedScore} | Blue: {BlueScore}", True, black)
    window.blit(score_text, (400, 10))
     
    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(60)
