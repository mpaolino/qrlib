'''
Created on 27.02.2010

@author: kerim
'''
from pysvg.turtle import Turtle, Vector
from pysvg.structure import svg

def testMultiplePaths():
    """
    -
     |
    -
    """
    t=Turtle()
    t.penDown()
    print(t.getPosition())
    t.forward(205)
    print(t.getPosition())
    t.right(90)
    t.forward(205)
    print(t.getPosition())
    t.right(90)
    t.forward(105)
    print(t.getPosition())
    t.right(90)
    t.forward(105)
    print(t.getPosition())
    t.penUp()
    t.moveTo(Vector(300,300))
    print(t.getPosition())
    t.penDown()
    t.forward(205)
    print(t.getPosition())
    t.finish()
    #print (t.getXML())
    s=svg(0, 0, 2000, 2000)
    s=t.addTurtlePathToSVG(s)
    s.save('./testoutput/testTurtle.svg')




def testLindenMayer():
    s=svg(0, 0, 2000, 2000)
    commands='F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F'
    t=Turtle()
    t.moveTo(Vector(500,250))
    t.penDown()
    angle=90
    distance=40
    for cmd in commands:
        print(cmd)
        if cmd=='F':
            t.forward(distance)
        elif cmd=='+':
            t.right(angle)
        elif cmd=='-':
            t.left(angle)
        print(t.getPosition())
    t.penDown()
    print (t.getXML())
    s=t.addTurtlePathToSVG(s)
    s.save('./testoutput/testTurtle.svg')


if __name__ == '__main__': 
    testLindenMayer()
    #testMultiplePaths()