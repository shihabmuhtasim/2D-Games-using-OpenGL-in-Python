from circle import MidpointCircle
from line import MidpointLine
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

WINDOW_X = 800
WINDOW_Y = 600

class Star:
    def __init__(self, x,num):
        self.star_color = (random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))
        self.x = x
        self.y = WINDOW_Y
        self.num = num

    def draw(self):
        color = self.star_color
        
        MidpointLine(self.x, self.y, self.x - 5, self.y - 15, color)
        MidpointLine(self.x, self.y, self.x + 5, self.y - 15,  color)

        MidpointLine(self.x - 5, self.y - 15, self.x-17, self.y - 15, color)
        MidpointLine(self.x + 5, self.y - 15, self.x + 17, self.y - 15,  color)

        MidpointLine(self.x - 17, self.y - 15, self.x - 8, self.y - 25, color)
        MidpointLine(self.x + 17, self.y - 15, self.x + 8, self.y - 25, color)

        MidpointLine(self.x - 8, self.y - 25, self.x - 10, self.y - 38, color)
        MidpointLine(self.x - 10, self.y - 38, self.x, self.y - 28, color)

        MidpointLine(self.x, self.y - 28, self.x + 10, self.y - 38, color)
        MidpointLine(self.x + 10, self.y - 38, self.x + 8, self.y - 25, color)

    def drawobstical3(self):
        color = self.star_color

        MidpointCircle(5, self.x , self.y-18, color) 
        MidpointLine(self.x, self.y, self.x - 10, self.y - 12, color)
        MidpointLine(self.x, self.y, self.x + 10, self.y - 12,  color)
        MidpointLine(self.x-10, self.y-12, self.x - 10, self.y - 37,  color)
        MidpointLine(self.x+10, self.y-12, self.x + 10, self.y - 37,  color)
        MidpointLine(self.x-10, self.y-37, self.x + 10, self.y - 37,  color)
        MidpointLine(self.x-10, self.y-34, self.x + 10, self.y - 34,  color)

        MidpointLine(self.x+10, self.y-37, self.x + 17, self.y - 40,  color)
        MidpointLine(self.x+10, self.y-25, self.x + 17, self.y - 28,  color)
        MidpointLine(self.x + 17, self.y - 40, self.x + 17, self.y - 28,  color)

        MidpointLine(self.x-10, self.y-37, self.x - 17, self.y - 40,  color)
        MidpointLine(self.x-10, self.y-25, self.x - 17, self.y - 28,  color)
        MidpointLine(self.x - 17, self.y - 40, self.x - 17, self.y - 28,  color)

        MidpointLine(self.x-7, self.y-37, self.x - 7, self.y - 40,  color)
        MidpointLine(self.x-3, self.y-37, self.x - 3, self.y - 40,  color)
        MidpointLine(self.x-3, self.y-40, self.x - 7, self.y - 40,  color)

        MidpointLine(self.x+7, self.y-37, self.x + 7, self.y - 40,  color)
        MidpointLine(self.x+3, self.y-37, self.x + 3, self.y - 40,  color)
        MidpointLine(self.x+3, self.y-40, self.x + 7, self.y - 40,  color)
    


    def drawobstical1(self):
        color = self.star_color

        MidpointCircle(4, self.x-8, self.y-29, color) 
        MidpointCircle(4, self.x+8, self.y-29, color) 

        MidpointLine(self.x, self.y, self.x - 17, self.y - 25, color)
        MidpointLine(self.x, self.y, self.x + 17, self.y - 25,  color)
        MidpointLine(self.x - 17, self.y - 25, self.x + 17, self.y - 25,  color)

        MidpointLine(self.x, self.y-6, self.x - 10, self.y - 20, color)
        MidpointLine(self.x, self.y-6, self.x + 10, self.y - 20,  color)
        MidpointLine(self.x - 10, self.y - 20, self.x + 10, self.y - 20,  color)

        MidpointLine(self.x-4, self.y-29, self.x - 8, self.y - 38, color)
        MidpointLine(self.x+4, self.y-29, self.x + 8, self.y - 38,  color)
        MidpointLine(self.x, self.y-25, self.x, self.y - 40,  color)




    # def drawobstical2(self):
    #     color = self.star_color

    #     MidpointCircle(5, self.x+2 , self.y-20, color) 
    #     MidpointLine(self.x+1, self.y, self.x - 5, self.y - 15, color)
    #     MidpointLine(self.x+1, self.y, self.x + 6, self.y - 10,  color)
    #     MidpointLine(self.x+13, self.y-5, self.x + 6, self.y - 10,  color)

    #     MidpointLine(self.x+10, self.y-15, self.x + 16, self.y - 12,  color)
    #     MidpointLine(self.x+10, self.y-20, self.x + 20, self.y - 20,  color)
    #     MidpointLine(self.x+10, self.y-25, self.x + 16, self.y - 30,  color)

    #     MidpointLine(self.x - 5, self.y - 15, self.x-17, self.y - 20, color)

    #     MidpointLine(self.x - 17, self.y - 20, self.x - 5, self.y - 25, color)

    #     MidpointLine(self.x - 5, self.y - 25, self.x+1 , self.y - 40, color)
    #     MidpointLine(self.x +1, self.y - 40, self.x+6, self.y - 30, color)
        
    #     MidpointLine(self.x +13, self.y - 35, self.x+6, self.y - 30, color)




class PowerUp:
    def __init__(self, x, y):
        self.power_color = (1.0, 0.0, 1.0)
        self.x = x
        self.y = y
        self.r = 50

    def draw(self):
        color = self.power_color
        MidpointCircle(self.r, self.x, self.y,color)

class Bullet:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.dir_x = a
        self.dir_y = b

    def draw(self):
        # print("Bullet x",self.x)
        # print("Bullet y",self.y)
        glPointSize(6.0)
        glBegin(GL_POINTS)
        glColor3f(1.0,1.0,1.0)
        glVertex2f(self.x, self.y)
        glEnd()

class SpaceShip:
    def __init__(self, game_paused,game_over):
        self.space_color = (0.0, 1.0, 1.0)
        self.x = 800//2         #inital center position
        self.y = 600//2
        #power flag
        self.power = False      #flag for special ball
        self.r = 25
        self.bullets_fired = []
        self.nose_x = self.x +400 
        self.nose_y = 65
        self.powerups = []
        self.paused = game_paused
        self.game_over=game_over
    def draw(self):
        color = self.space_color

        spaceship_position = self.x
        MidpointCircle(25, 400 + spaceship_position, 25, color)
        MidpointLine(375 + spaceship_position, 25, 425 + spaceship_position, 25, color)
        MidpointLine(355 + spaceship_position, 15, 445 + spaceship_position, 15, color)
        MidpointLine(445 + spaceship_position, 15, 425 + spaceship_position, 25, color)
        MidpointLine(355 + spaceship_position, 15, 375 + spaceship_position, 25, color)

        MidpointLine(399 + spaceship_position, 60, 399 + spaceship_position, 50, color)
        MidpointLine(401 + spaceship_position, 60, 401 + spaceship_position, 50, color)
        MidpointCircle(5, 400 + spaceship_position, 65, color)




        if not self.paused and not self.game_over:
            for bullet in self.bullets_fired:
                if bullet.x > WINDOW_X or bullet.x < 0 or bullet.y > WINDOW_Y:
                    self.bullets_fired.remove(bullet)
                else:
                    bullet.x += bullet.dir_x 
                    bullet.y += bullet.dir_y
                    # print("bullet  y",bullet.y)
                    # print("bullet direction y",bullet.dir_y)
                    bullet.draw()
                    

    def fire(self, dir_x, dir_y):
        bullet = Bullet(self.nose_x, self.nose_y, dir_x, dir_y)
        self.bullets_fired.append(bullet)

    def powerup(self):
        if self.power == True and self.nose_x>40:

            ball = PowerUp(self.nose_x, self.nose_y)
            self.powerups.append(ball)
            self.power = False
