from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from line import MidpointLine
from classes import  SpaceShip, Star, PowerUp
import random
import time

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
    no_of_star = random.randint(2,5)
    create_stars(no_of_star)

    glutPostRedisplay()

def display():
    global click,power_instance,circle_drawn_time,score ,no_of_star, game_over, count

    if game_over:
        glClearColor(1.0, 1.0, 1.0, 0.0)
        spaceship.space_color = (1.0, 0.0, 0.0) 

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

no_of_star = random.randint(2,5)

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

    # Limit the updates 
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