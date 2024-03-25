# Projectile Motion

import math
import random
import pygame

#----------------------------------------------------------------
# math part
radius = 160

def toRadian(theta):
    return theta * math.pi / 180

def toDegrees(theta):
    return theta * 180 / math.pi

def getGradient(p1, p2):
    if p1[0] == p2[0]:
        m = toRadian(90)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m

def getAngleFromGradient(gradient):
    return math.atan(gradient)

def getAngle(pos, origin):
    m = getGradient(pos, origin)
    thetaRad = getAngleFromGradient(m)
    theta = round(toDegrees(thetaRad), 2)
    return theta

def getPosOnCircumeference(theta, origin):
    theta = toRadian(theta)
    x = origin[0] + radius * math.cos(theta)
    y = origin[1] + radius * math.sin(theta)
    return (x, y)

# ----------------------------------------------------------------
# pygame part

# screen size n stuff
pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

# clock and fps
clock = pygame.time.Clock()
FPS = 60

# colours
BLACK = (18, 18, 18)
WHITE = (217, 217, 217)
RED = (252, 91, 122)
GREEN = (29, 161, 16)
BLUE = (78, 193, 246)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,249,182)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE]

# set origin as player center
origin = (20, 340)
# no fucking idea what this does
radius = 50

# arch distance modifier
u = 50
# gravity modifier
g = 9.8

class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta):
        super(Projectile, self).__init__()

        self.u = u
        self.theta = toRadian(abs(theta))
        self.x, self.y = origin

        # no idea what this does
        self.ch = 0
        # speed
        self.dx = 5
        
        self.f = self.getTrajectory()
        self.range = self.x + abs(self.getRange())

        self.path = []

    def timeOfFlight(self):
        return round((2 * self.u * math.sin(self.theta)) / g, 2)

    def getRange(self):
        range_ = ((self.u ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g
        return round(range_, 2)

    def getMaxHeight(self):
        h = ((self.u ** 2) * (math.sin(self.theta)) ** 2) / (2 * g)
        return round(h, 2)

    def getTrajectory(self):
        return round(g /  (2 * (self.u ** 2) * (math.cos(self.theta) ** 2)), 4)

    def getProjectilePos(self, x):
        return x * math.tan(self.theta) - self.f * x ** 2

    def update(self):
        if self.x >= self.range:
            self.dx = 0
        self.x += self.dx
        self.ch = self.getProjectilePos(self.x - origin[0])

        self.path.append((self.x, self.y-abs(self.ch)))
        self.path = self.path[-50:]

        pygame.draw.circle(win, WHITE, self.path[-1], 5)
        pygame.draw.circle(win, WHITE, self.path[-1], 5, 1)
        for pos in self.path[:-1:5]:
            pygame.draw.circle(win, WHITE, pos, 1)

projectile_group = pygame.sprite.Group()

clicked = False
currentp = None

theta = -30
end = getPosOnCircumeference(theta, origin)
arct = toRadian(theta)
arcrect = pygame.Rect(origin[0]-30, origin[1]-30, 60, 60)

running = True
while running:
    win.fill(BLACK)
    
    for event in pygame.event.get():
            
        # quit button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

            pos = event.pos
            theta = getAngle(pos, origin)
            if -90 < theta <= 0:
                projectile = Projectile(u, theta)
                projectile_group.add(projectile)
                currentp = projectile

        if event.type == pygame.MOUSEMOTION:
            if clicked:
                pos = event.pos
                theta = getAngle(pos, origin)
                if -90 < theta <= 0:
                    end = getPosOnCircumeference(theta, origin)
                    arct = toRadian(theta)
    

    pygame.draw.line(win, AQUA, origin, end, 2)
    pygame.draw.circle(win, WHITE, origin, 3)
    pygame.draw.arc(win, AQUA, arcrect, 0, -arct, 2)

    projectile_group.update()


    pygame.draw.rect(win, (0,0,0), (0, 0, WIDTH, HEIGHT), 5)
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()
