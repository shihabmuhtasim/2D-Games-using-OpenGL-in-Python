from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
