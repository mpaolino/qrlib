#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pysvg.structure import *
from pysvg.shape import *

import math

def testClipPath():
    mySVG = svg("a spiral with clipping")
    group = g()
    pathId = "pathTriangle"
    myPath = path(pathData= "M 0 0 L 450 450 L 900 0" )
    clip = clipPath(id="pathTriangle")
    clip.addElement(myPath)
    clip.set_id(pathId)
    myDef=defs()
    myDef.addElement(clip)
    mySVG.addElement(myDef)
    group.set_clip_path("url(#%s)" % pathId)
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
        group.addElement(c)
    mySVG.addElement(group)
    mySVG.save('./testoutput/spiralClipped.svg')
  
if __name__ == '__main__': 
  testClipPath()
  
