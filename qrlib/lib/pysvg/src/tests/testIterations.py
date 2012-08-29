#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pysvg.structure import *
from pysvg.shape import *
from pysvg.builders import ShapeBuilder

import math

def testIterationsWithUse():
    s=svg()
    d = defs()
    sb =ShapeBuilder()
    rectangle = sb.createRect(0,0,100,200,fill='000')
    rectangle.set_id('baseRect')
    d.addElement(rectangle)
    s.addElement(d)
    coords=[(1,1),(200,200)]
    for (x,y) in coords:
        r=use()
        r.set_x(x)
        r.set_y(y)
        r.set_xlink_href('#baseRect')
        s.addElement(r)

    s.save('./testoutput/iterationsWithUse.svg')


def testIterationsWithAttributesChange():
    s=svg()
    
    sb =ShapeBuilder()
    coords=[(1,1),(200,200)]
    for (x,y) in coords:
        rectangle = sb.createRect(0,0,100,200,fill='000')
        rectangle.set_x(x)
        rectangle.set_y(y)
        s.addElement(rectangle)

    s.save('./testoutput/iterationsWithAttributesChange.svg')

  
if __name__ == '__main__': 
  testIterationsWithUse()
  testIterationsWithAttributesChange()
  
