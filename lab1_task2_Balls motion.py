from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

# Define global variables
box_color = (0.0, 0.0, 0.0)  # Background color
points = [] #point init
point_speed = 0.0001 #move init
blink_speed = 1.0  # time in seconds for  blink- later convert in milisec
blink_on = False  # blinkFlag 
c_blink = None #check blink init flag
space_pressed = False  #  freezing flag


# Initialize OpenGL
glutInit()
glutInitWindowSize(800, 600)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"Interactive Box")

# Function for blink on off repeatedly
def toggle_blink_state(value):
    #if c_clink =0
    if c_blink is not None:
        global blink_on
        #when b_on true it becomes false, and when false it becomes true 
        #THEN draw func once makes it black then again makes it balls
        blink_on = not blink_on
        glutTimerFunc(int(blink_speed * 1000), toggle_blink_state, 0)
    else:
        blink_on = False


# defined func for randomly generating color
def random_color():
    return (random.random(), random.random(), random.random())

# diagonal movement possiblities- multiply the speed val with it
def random_direction():
    return (random.choice([1, -1]), random.choice([1, -1]))

# draw pouints
def draw_point(position, color):
    if not space_pressed:  # draw when not frozen 
        if blink_on: #this is while blink already going on - using toggle func
            glColor3f(0.0, 0.0, 0.0)  # Set color to black 
        else: #unblinked
            glColor3fv(color)  
            glBegin(GL_POINTS)
            glVertex3fv(position) #pos gets x,y from display func
            glEnd()
    #when freezed
    else:
        glColor3fv(color)  # Use the original color
        glBegin(GL_POINTS)
        glVertex3fv(position)
        glEnd()



#update the point positions
def update_points():
    if not space_pressed:  # if points should not be frozen
        for i in range(len(points)):
            x, y, color, direction = points[i] #unpack from points
            new_x = x + point_speed * direction[0] #making points move (direction has diagonal axis and mul w speed gives a coordinate )
            new_y = y + point_speed * direction[1]

            # bounce back
            if abs(new_x) >= 1:
                direction = (-direction[0], direction[1])
            if abs(new_y) >= 1:
                direction = (direction[0], -direction[1])

            points[i] = (new_x, new_y, color, direction)


def mouse_click(button, state, x, y):
    global blink_on, c_blink
    if not space_pressed:  # when points not frozen
        if state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON:
            #to start the point
            x = (x/800)
            y = y/600
            #print("x",x)
            #print("y",y)
            color = random_color()
            direction = random_direction()
            points.append((x, y, color, direction))
        elif state == GLUT_DOWN and button == GLUT_LEFT_BUTTON:
            # if blink is not already started
            if c_blink is None:
                c_blink = 0
                #first call glut timer func
                glutTimerFunc(int(blink_speed * 1000), toggle_blink_state, 0)
                

            else:
                # if already blinking then make c_blink to 0 then toggle func auto wont work 
                c_blink = None



def specialKeyListener(key, x, y):
    global point_speed, space_pressed
    if not space_pressed:
        if key == GLUT_KEY_UP:
            point_speed += 0.0001
        elif key == GLUT_KEY_DOWN:
            if point_speed > 0.0002:
                point_speed -= 0.0001


#space hold
def keyboardListener(key, x, y):
    global space_pressed
    if key==b" ": 
        space_pressed = not space_pressed

# Main display function
def display():
    global box_color, points 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #as points are moving , updating points each time and drawing the points by calling draw func
    update_points()
    for x, y, color, _ in points:
        glPointSize(7.0)
        draw_point((x, y, 0), color) #sending to draw_point func (x,y,z axis)
    glutSwapBuffers() #without this the window doesnt work

# calling functions
glutDisplayFunc(display)
glutIdleFunc(glutPostRedisplay)
glutMouseFunc(mouse_click)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)

# Start the main loop
glutMainLoop()
