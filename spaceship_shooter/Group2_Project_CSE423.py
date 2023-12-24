from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time



def findzone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx >= 0:
        if dy >= 0:
            return 0 if abs(dx) > abs(dy) else 1
        else:
            return 7 if abs(dx) > abs(dy) else 6
    else:
        if dy >= 0:
            return 3 if abs(dx) > abs(dy) else 2
        else:
            return 4 if abs(dx) > abs(dy) else 5

def convert_to_zone0(x, y, original_zone):
    if original_zone == 0:
        return (x, y)
    elif original_zone == 1:
        return (y, x)
    elif original_zone == 2:
        return (y, -x)
    elif original_zone == 3:
        return (-x, y)
    elif original_zone == 4:
        return (-x, -y)
    elif original_zone == 5:
        return (-y, -x)
    elif original_zone == 6:
        return (-y, x)
    elif original_zone == 7:
        return (x, -y)

def convert_to_original_zone(x, y, original_zone):
    if original_zone == 0:
        return (x, y)
    elif original_zone == 1:
        return (y, x)
    elif original_zone == 2:
        return (-y, x)
    elif original_zone == 3:
        return (-x, y)
    elif original_zone == 4:
        return (-x, -y)
    elif original_zone == 5:
        return (-y, -x)
    elif original_zone == 6:
        return (y, -x)
    elif original_zone == 7:
        return (x, -y)

def drawpixel(x, y, original_zone):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def MidpointLine(x1, y1, x2, y2, color):
    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convert_to_zone0(x1, y1, zone)
    x2, y2 = convert_to_zone0(x2, y2, zone)
    glColor3f(*color)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x = x1
    y = y1
    
    while x < x2:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        original_x, original_y = convert_to_original_zone(x, y, zone)
        drawpixel(original_x, original_y, zone)

def plotPoints(x, y, xc, yc):
    glVertex2f(x + xc, y + yc)
    glVertex2f(y + xc, x + yc)
    glVertex2f(-y + xc, x + yc)
    glVertex2f(-x + xc, y + yc)
    glVertex2f(-x + xc, -y + yc)
    glVertex2f(-y + xc, -x + yc)
    glVertex2f(y + xc, -x + yc)
    glVertex2f(x + xc, -y + yc)

def MidpointCircle(radius, xc, yc, color):
    x = 0
    y = radius
    d = 1 - radius
    glColor3f(*color)

    glBegin(GL_POINTS)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * (x - y) + 5
            x += 1
            y -= 1
        plotPoints(x, y, xc, yc)
    glEnd()

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




    def drawobstical2(self):
        color = self.star_color

        MidpointCircle(5, self.x+2 , self.y-20, color) 
        MidpointLine(self.x+1, self.y, self.x - 5, self.y - 15, color)
        MidpointLine(self.x+1, self.y, self.x + 6, self.y - 10,  color)
        MidpointLine(self.x+13, self.y-5, self.x + 6, self.y - 10,  color)

        MidpointLine(self.x+10, self.y-15, self.x + 16, self.y - 12,  color)
        MidpointLine(self.x+10, self.y-20, self.x + 20, self.y - 20,  color)
        MidpointLine(self.x+10, self.y-25, self.x + 16, self.y - 30,  color)

        MidpointLine(self.x - 5, self.y - 15, self.x-17, self.y - 20, color)

        MidpointLine(self.x - 17, self.y - 20, self.x - 5, self.y - 25, color)

        MidpointLine(self.x - 5, self.y - 25, self.x+1 , self.y - 40, color)
        MidpointLine(self.x +1, self.y - 40, self.x+6, self.y - 30, color)
        
        MidpointLine(self.x +13, self.y - 35, self.x+6, self.y - 30, color)




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



WINDOW_X = 800
WINDOW_Y = 600

game_paused = False
game_over = False
score=0
count=0

spaceship = SpaceShip(game_paused,game_over)
stars = []
star_1=1
star_2=3
click=False
power_instance=None
circle_drawn_time = 0


def draw_left_arrow():
    color = (0.8, 0.7, 0.0)
    MidpointLine(10, 580, 35, 580, color)
    MidpointLine(10, 580, 20, 590, color)
    MidpointLine(10, 580, 20, 570, color)
    

def draw_pause_symbol():
    color = (0.0, 1.0, 0.0)
    MidpointLine(10, 520, 10, 550, color)
    MidpointLine(35, 520, 35, 550, color)

def draw_play_symbol():
    color = (1.0, 0.65, 0.0)
    MidpointLine(10, 520, 10, 550, color)
    MidpointLine(35, 535, 10, 550, color)
    MidpointLine(35, 535, 10, 520, color)

def draw_cross():
    color = (1.0, 0.5, 0.5)
    MidpointLine(10, 500, 35, 475, color)
    MidpointLine(35, 500, 10, 475, color)

def draw_heart1():
    color = (1.0, 0.0, 0.0)
    MidpointLine(10, 445, 22, 430, color)
    MidpointLine(10, 445, 16, 452, color)
    MidpointLine(16, 452, 22, 445, color)
    MidpointLine(34, 445, 28, 452, color)
    MidpointLine(28, 452, 22, 445, color)
    MidpointLine(22, 430, 34, 445, color)

def draw_heart2():
    color = (1.0, 0.0, 0.0)
    MidpointLine(10, 415, 22, 400, color)
    MidpointLine(10, 415, 16, 422, color)
    MidpointLine(16, 422, 22, 415, color)
    MidpointLine(34, 415, 28, 422, color)
    MidpointLine(28, 422, 22, 415, color)
    MidpointLine(22, 400, 34, 415, color)

def draw_heart3():
    color = (1.0, 0.0, 0.0)
    MidpointLine(10, 385, 22, 370, color)
    MidpointLine(10, 385, 16, 392, color)
    MidpointLine(16, 392, 22, 385, color)
    MidpointLine(34, 385, 28, 392, color)
    MidpointLine(28, 392, 22, 385, color)
    MidpointLine(22, 370, 34, 385, color)





def togglePause():
    global game_paused, spaceship
    game_paused = not game_paused
    spaceship.paused = game_paused
    if game_paused:
        print("Game Paused")
    else:
        print("Game Resumed")

def restartGame():
    global game_over, stars , star_speed, spaceship, game_paused, score, star_1, star_2, count
    game_paused=False
    game_over = False
    score = 0
    count = 0
    star_1 = 1
    star_2 = 3
    spaceship = SpaceShip(game_paused,game_over)
    stars = []
    no_of_star = 3
    create_stars(no_of_star)

    glutPostRedisplay()

def display():
    global click,power_instance,circle_drawn_time,score ,no_of_star, game_over, count

    if game_over:
        glClearColor(1.0, 1.0, 1.0, 0.0) 
    else:
        glClearColor(0.0, 0.0, 0.0, 0.0)  

    glClear(GL_COLOR_BUFFER_BIT)
    spaceship.draw()

    #drawing buttons
    if count == 0:
        draw_heart1()
        draw_heart2()
        draw_heart3()
    elif count == 1:
        draw_heart1()
        draw_heart2()
    elif count == 2:
        draw_heart1()
    
    
    draw_left_arrow()
    if not game_paused:
        draw_pause_symbol()
    else:
        draw_play_symbol() 
    draw_cross()

    #drawing stars
    if not game_over:
        
        for star in stars:
            
            if power_instance is not None:
                new_x=power_instance.x
                new_y=power_instance.y
                if star.y-30<=new_y+50 and star.x+15>=new_x-50 and star.x-15<=new_x+50 and star.y>=new_y-50:

                    score+=2
                    print("Bonus catch!!!")
                    print("Score:",score)
                    stars.remove(star)
                    no_of_star -= 1

           
            if star.num%2==0:    
                star.draw()
            elif star.num%3==0:
                star.drawobstical1()
            elif star.num%4==0:
                star.drawobstical2() 
            else:
                star.drawobstical3()

        if click==True:
            power_instance.draw()
            
            circle_drawn_time = time.time()
            click=False
        if power_instance is not None and time.time() - circle_drawn_time <= 5:
            power_instance.draw()
            
        elif power_instance is not None and time.time() - circle_drawn_time > 5:
            
            power_instance=None
         

    glutSwapBuffers()

no_of_star = 3

def create_stars(n):
    for i in range(n):
        star = Star(random.randint(5, WINDOW_X-5),i)    #creating a star object
        stars.append(star) 


create_stars(no_of_star)   



def updateGame(value):
    global no_of_star, stars, game_over, game_paused,score, star_1, star_2, count

    if not game_over and not game_paused:
        # print('before hitting star:', no_of_star)
        #checking for bullet and star collision
        for bullet in spaceship.bullets_fired:
            for star in stars:
                if bullet.x > star.x-15 and bullet.x < star.x+15 and bullet.y > star.y-30 and bullet.y < star.y:
                    print('Hit!!')
                    score+=1
                    print("Score:", score)

                    if score%5==0 and score!=0:
                        spaceship.power=True
                        print("Power Gained!!")

                    if score%5==0 and score!=0:
                        star_1+=1
                        star_2+=1
                        print("Speed Increased :()")

                    
                    spaceship.bullets_fired.remove(bullet)
                    stars.remove(star)
                    no_of_star -= 1
                    
                  

        
        #updating star positoins
        for star in stars:
            speed = random.randint(star_1,star_2)
            star.y -= speed
            if star.y < 0:
                count += 1
                stars.remove(star)
                no_of_star -= 1
                print("Lost",count,"heart!")
            if count == 3:
                game_over = True
                print("Game Over!")
                print("Total score", score)

        #drawing new stars
        if no_of_star <= 0:
            no_of_star = random.randint(1, 5)
            create_stars(no_of_star)

    elif game_over:
             #update needed. the game should not close
        glutIdleFunc(None)

    glutTimerFunc(30, updateGame, 0)
    glutPostRedisplay()



def specialKeyListener(key, x, y):

    global spaceship_position
    if not game_paused and not game_over:
        if key == GLUT_KEY_LEFT:
            
            spaceship.fire(-2,2)
            
        elif key == GLUT_KEY_RIGHT:
            
            spaceship.fire(2,2)

        elif key == GLUT_KEY_UP:
            
            spaceship.fire(0,2)

last_update_time = time.time()

def mouseMotion(x, y):
    global spaceship_position, last_update_time

    # Limit the updates to a certain frame rate (e.g., 30 frames per second)
    current_time = time.time()
    time_elapsed = current_time - last_update_time

    if time_elapsed > 1 / 30:  # 30 frames per second
        last_update_time = current_time

        if not game_over and not game_paused:
            spaceship_position = x - 400

            # Boundary condition
            if spaceship_position < -355:
                spaceship_position = -355
            elif spaceship_position > 355:
                spaceship_position = 355

            spaceship.x = spaceship_position
            spaceship.nose_x = spaceship_position + 400

            glutPostRedisplay()


def mouseClick(button, state, x, y):
    global game_over, game_paused, power_instance, click

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:


        glutPostRedisplay()
        

        if 10 <= x <= 35 and 10 <= y <= 30: 
            print("Starting over!")
            restartGame()

        elif 10 <= x <= 35 and 50 <= y <= 80: 
            togglePause()

        elif 10 <= x <= 35 and 100 <= y <= 125:  
            print("Goodbye!")
            glutLeaveMainLoop()

        elif x>=30:
            if spaceship.power==True:
                power_instance=PowerUp(x,600-y)
                click=True
                
                print(x,y)


                spaceship.power=False



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WINDOW_X, WINDOW_Y)
glutCreateWindow(b"423 Project")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0, 800, 0, 600)
glutDisplayFunc(display)
glutPassiveMotionFunc(mouseMotion)
glutMouseFunc(mouseClick)
glutTimerFunc(0, updateGame, 0)
glutSpecialFunc(specialKeyListener)
glutMainLoop()