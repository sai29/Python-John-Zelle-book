

import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def area(perimeter,p1,p2,p3):
    s = perimeter / 2
    a = math.sqrt(float(s*(s-p1)*(s-p2)*(s-p3)))
    return a

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p3,p1)
    area1 = area(perim,d1,d2,d3) 
    message.setText("The perimeter is: %0.2f" % perim)
    win.getMouse()
    message.setText("The area is: %0.2f" % area1)

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
