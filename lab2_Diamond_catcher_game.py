from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutLeaveMainLoop
import random
diamond_x = random.randint(0, 750)
diamond_y = 600  # y of the diamond
diamond_speed = 5  # Speed at which the diamond falls
#coordinates for plate
holder_plate_x1 = 300
holder_plate_x2 = 420
holder_plate_y1 = 60
holder_plate_y2 = 40

elapsed_time = 0
score = 0
game_over = False
game_paused = False
#starting colour
diamond_colour=(1.0, 0.75, 0.8)


def setPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()



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
    
def drawMidpointLine(x1, y1, x2, y2):
    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convert_to_zone0(x1, y1, zone)
    x2, y2 = convert_to_zone0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)

    x, y = x1, y1

    #setPixel(x, y)
    while x < x2:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        new_x, new_y = convert_to_original_zone(x, y, zone)
        setPixel(new_x, new_y)

def drawHolderPlate():
    # upper line 
    drawMidpointLine(holder_plate_x1, holder_plate_y1, holder_plate_x2, holder_plate_y1)

    #lower line 
    drawMidpointLine(holder_plate_x1 + 20, holder_plate_y2, holder_plate_x2 - 20, holder_plate_y2)

    # Connect
    drawMidpointLine(holder_plate_x1 + 20, holder_plate_y2, holder_plate_x1, holder_plate_y1)
    drawMidpointLine(holder_plate_x2 - 20, holder_plate_y2, holder_plate_x2, holder_plate_y1)

def drawDiamond():
    # Draw diamond 
    drawMidpointLine(diamond_x, diamond_y, diamond_x + 20, diamond_y + 20)
    drawMidpointLine(diamond_x + 20, diamond_y - 20, diamond_x, diamond_y)
    drawMidpointLine(diamond_x + 40, diamond_y, diamond_x + 20, diamond_y + 20)
    drawMidpointLine(diamond_x + 20, diamond_y - 20, diamond_x + 40, diamond_y)

def display():
    global game_over, diamond_colour
    glClear(GL_COLOR_BUFFER_BIT)

    if not game_over:
        
        glColor3f(*diamond_colour)
        drawDiamond()
        glColor3f(0.0, 0.0, 1.0)
        # restart button
        drawMidpointLine(50, 550, 100, 550)
        drawMidpointLine(50, 550, 70, 570)
        drawMidpointLine(70, 530, 50, 550)
        glColor3f(1.0, 0.0, 0.0)
        # terminate button
        drawMidpointLine(700, 530, 750, 570)
        drawMidpointLine(750, 530, 710, 570)


        glColor3f(1.0, 1.0, 1.0)
        drawHolderPlate()


        # diamond caught
        if (
            diamond_x >= holder_plate_x1
            and diamond_x + 40 <= holder_plate_x2
            and diamond_y <= holder_plate_y1
            
        ):
            global score, diamond_speed
            score += 1
            print("Score:", score)
            diamond_reset()
            diamond_speed+=0.2
            diamond_colour=(random.random(), random.random(), random.random())

        # diamond misses the holder plate
        if diamond_y < holder_plate_y2:
            game_over = True
            print("Game Over!")
            print("Final Score: ",score)
            glColor3f(1.0, 0.0, 0.0)
            drawHolderPlate()
            glutIdleFunc(None)  # Pause the game
            
        glColor3f(1.0, 1.0, 0.0)
        if not game_paused:
            # pause button
            drawMidpointLine(400, 530, 400, 580)
            drawMidpointLine(420, 530, 420, 580)
        elif game_paused:
            #play button
            drawMidpointLine(400, 530, 400, 580)
            drawMidpointLine(400, 530, 430, 550)
            drawMidpointLine(430, 550, 400, 580)

    glutSwapBuffers()

def updateGame(value):
    if not game_over and not game_paused:
        global diamond_y,elapsed_time
        diamond_y -= diamond_speed 
        glutPostRedisplay()
        glutTimerFunc(16, updateGame, 0)  # 60 frames per second


def specialKey(key, x, y):
    global holder_plate_x1, holder_plate_x2, game_paused

    if not game_over and not game_paused:
        if key == GLUT_KEY_LEFT:
            change =- 100
        elif key == GLUT_KEY_RIGHT:
            change = 100
        dx = holder_plate_x2 - holder_plate_x1
        holder_plate_x1 = holder_plate_x1+change
        holder_plate_x2 = holder_plate_x1 + dx
        

        glutPostRedisplay()

def togglePause():
    global game_paused
    game_paused = not game_paused
    if game_paused:
        print("Game Paused")
    else:
        print("Game Resumed")
        glutTimerFunc(0, updateGame, 0)

def restartGame():
    global game_over, score, diamond_speed
    game_over = False
    score = 0
    diamond_speed=5
    diamond_reset()
    

def diamond_reset():
    global diamond_x, diamond_y, diamond_colour
    
    diamond_x = random.randint(0, 750)
    diamond_y = 600
    

def mouseClick(button, state, x, y):
    global game_over
    #print(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 399 <= x <= 500 and 30 <= y <= 80:  # Pause button
            togglePause()
        elif 20 <= x <= 100 and 20 <= y <= 70:  # Restart button
            restartGame()
        elif 650 <= x <= 750 and 10 <= y <= 70:  # Restart button
            glutLeaveMainLoop()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 800, 0, 600)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"2D game of dimond catching")
glutDisplayFunc(display)
glutSpecialFunc(specialKey)
glutMouseFunc(mouseClick)
init()
glutTimerFunc(0, updateGame, 0)
glutMainLoop()
