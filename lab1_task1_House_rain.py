from OpenGL.GL import *
from OpenGL.GLUT import *
import random

#vars
background_color = (0.0, 0.0, 0.0)
door_color = (0.855, 0.647, 0.125)
house_color = (0.5, 0.5, 0.5)  #gray
roof_color = (0.7, 0.1, 0.1)  #red
rain_color = (0.0, 0.0, 1.0)  #blue
rain_x1 = [0.0] * 30  # X-coordinates of raindrop start points
rain_y1 = [0.0] * 30  # Y-coordinates of raindrop start points
rain_x2 = [0.0] * 30 # X2-coordinates of raindrop end points
rain_y2 = [0.0] * 30  # Y3-coordinates of raindrop end points
num_raindrops = 30 # 30 rain drops generate in an iteration


def drawBackground():
    glColor3fv(background_color)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()


   
def drawHouse():
    # House 
    glColor3fv(house_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.35, 0.2)
    glVertex2f(-0.35, -0.2)
    glVertex2f(0.0, 0.2)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0.35, 0.2)
    glVertex2f(0.35, -0.2)
    glVertex2f(0.0, 0.2)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.35, -0.2)
    glVertex2f(0.35, -0.2)
    glVertex2f(0.0, 0.2)
    glEnd()

    #door
    glColor3fv(door_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.2)
    glVertex2f(-0.05, 0.1)
    glEnd()
   
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.2)
    glVertex2f(0.05, 0.1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.05, 0.1)
    glVertex2f(0.05, 0.1)
    glVertex2f(0.0, -0.2)
    glEnd()

    #draw knob
    glPointSize(6) #pixel size. by default 1 thake
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(0.02,-0.02) #jekhane show korbe pixel
    glEnd()


    #window
    glColor3fv(door_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.15, -0.05)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.1, -0.05)
    glVertex2f(0.15, -0.05)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0.2, -0.05)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.15, -0.05)
    glEnd()

    #window lines
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.15, 0.1)
    glVertex2f(0.15, -0.05)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(0.1, 0.025)
    glVertex2f(0.2, 0.025)
    glEnd()


    # Roof
    glColor3fv(roof_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.35, 0.2)
    glVertex2f(0.35, 0.2)
    glVertex2f(0.0, 0.5)
    glEnd()

def drawRain():
    glColor3fv(rain_color)
    glLineWidth(1)
    glBegin(GL_LINES)
    # 3 layers of rain
    for j in range(3):
        #total 30 points draw each layer
        for i in range(num_raindrops):
            glVertex2f(rain_x1[i], rain_y1[i])
            glVertex2f(rain_x2[i], rain_y2[i])
        
        #updating rain points for the next iteration
        for k in range(30):
            x=random.uniform(0,0.5)
            rain_y1[k]=rain_y1[k]-x
            rain_y2[k]=rain_y2[k]-x
        
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    drawBackground()
    # Draw the house
    drawHouse()
    # Draw the rain
    drawRain()
    glutSwapBuffers()

def initializeRain():
    for i in range(num_raindrops):
        rain_x1[i] =random.uniform(-1, 1) #randomly take a value in the range
        rain_y1[i] = 1.0 #up 
        rain_x2[i] = rain_x1[i] #same as x1
        rain_y2[i] = rain_y1[i] - 0.1 #down
   

def changeRainDirection(direction):

        
        if direction == -1:
            for i in range(30):
                rain_x2[i] = rain_x2[i] - 0.05
            
        elif direction == 1:
            for j in range(30):
                rain_x2[j] = rain_x2[j] + 0.05
        
        


def specialKeyListener(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction = -1
        
        
    elif key == GLUT_KEY_RIGHT:
        rain_direction = 1
        

    initializeRain()

    changeRainDirection(rain_direction)

    glutPostRedisplay()

def keyboardListener(key, x, y):

    global background_color
    if key==b" ": 
        print("GOT SPACEBAR")
    if key==b'n':
        background_color = (background_color[0] - 0.2, background_color[1] - 0.2, background_color[2] - 0.2)
        
        print("day")
    if key==b'd':
        background_color = (background_color[0] + 0.2, background_color[1] + 0.2, background_color[2] + 0.2)
        
        print("night")
    initializeRain()
    glutPostRedisplay()

def mouse_click(button, state, x, y):
    initializeRain()
    glutPostRedisplay()


#init   
glutInit()
glutInitWindowSize(800, 800)
glutCreateWindow(b"House and Rain")

#call func
glutDisplayFunc(display)

glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)


# Initialize raindrop positions
initializeRain()
glutMouseFunc(mouse_click)

glutMainLoop()


