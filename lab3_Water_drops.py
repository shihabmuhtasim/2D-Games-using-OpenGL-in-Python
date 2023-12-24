from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# [x, y, radius]
circles = []
radius = 10
game_paused=False
speed=0.3
# convert
def plotPoints(x, y, xc, yc):
    glVertex2f(x + xc, y + yc)
    glVertex2f(y + xc, x + yc)
    glVertex2f(-y + xc, x + yc)
    glVertex2f(-x + xc, y + yc)
    glVertex2f(-x + xc, -y + yc)
    glVertex2f(-y + xc, -x + yc)
    glVertex2f(y + xc, -x + yc)
    glVertex2f(x + xc, -y + yc)

def MidpointCircle(radius, xc, yc):
    x = 0
    y = radius
    d = 1 - radius

    # Initial points
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

# Timer update radius and remove circles
def updateCircles(value):
    global circles, radius, game_paused, speed
    if not game_paused:
        # Update  radius 
        for circle in circles:
            circle[2] += speed  

    #remove
    new_circles = []  # approved ones store here

    for circle in circles:  
        x, y, r = circle  # Extract
        # Check
        if 0 <= x - r < 800 and 0 <= x + r < 800 and 0 <= y - r < 600 and 0 <= y + r < 600:
            new_circles.append(circle) 

    circles = new_circles 

    glutPostRedisplay()
    glutTimerFunc(16, updateCircles, 0) 

# Display function
def display():
    global circles
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 0.7, 1.0)

    # Draw 
    for circle in circles:
        MidpointCircle(circle[2], circle[0], circle[1])

    glutSwapBuffers()


def mouseClick(button, state, x, y):
    global circles, radius,game_paused
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        #[x, y, radius]
        #print(x,y)
        if not game_paused:
            circles.append([x, 600 - y, radius])
            glutPostRedisplay()


def keyboardListener(key, x, y):
    global game_paused
    if key==b" ": 
        game_paused = not game_paused


def specialKey(key, x, y):
    global game_paused, speed
    if not game_paused:
        if key == GLUT_KEY_UP:
            speed +=0.3
        elif key == GLUT_KEY_DOWN:
            if speed<=0.3:
                pass
            
            else:
                speed -=0.3
        

    glutPostRedisplay()
    
# Initialization
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Multiple Circles")

glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0, 800, 0, 600)


glutDisplayFunc(display)
glutMouseFunc(mouseClick)
glutSpecialFunc(specialKey)
glutKeyboardFunc(keyboardListener)
glutTimerFunc(0, updateCircles, 0)

glutMainLoop()
