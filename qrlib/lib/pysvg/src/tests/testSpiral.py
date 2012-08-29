#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pysvg.structure import *
from pysvg.shape import *

import math

def testSpiral():
  mySVG = svg("a spiral")
  
  for i in range(1, 200):
    x = 2 * i * math.cos(2 * math.pi * i / 40.5) + 450
    y = 2 * i * math.sin(2 * math.pi * i / 40.5) + 450
    #print 'color: rgb(%s,%s,%s)' % (i, 200-i, i*(200-i)/50)
    c = circle(x, y, 0.2 * i)
    fill = 'none'
    strokewidth = 5 
    stroke = 'rgb(%s,%s,%s)' % (i, 200 - i, i * (200 - i) / 50)
    myStyle = 'fill:%s;stroke-width:%s; stroke:%s' % (fill, strokewidth, stroke)
    c.set_style(myStyle)
    mySVG.addElement(c)

  mySVG.save('./testoutput/spiral.svg')
  
if __name__ == '__main__': 
  testSpiral()
  
