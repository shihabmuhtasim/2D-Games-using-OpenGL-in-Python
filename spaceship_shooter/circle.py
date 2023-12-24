from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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
