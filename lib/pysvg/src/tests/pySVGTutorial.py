#!/usr/bin/python
# -*- coding: iso-8859-1 -*-


from pysvg.filter import *
from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *

class MyDropShadow(filter):    
    def __init__(self):
        filter.__init__(self)
        self.set_x('-0.25')
        self.set_y('-0.25')
        self.set_width(3)
        self.set_height(3)
        self.set_id('MyDropShadow')
        self.myGauss = feGaussianBlur()
        self.myGauss.set_id('DropShadowGauss')
        self.myGauss.set_stdDeviation(1.0)
        self.myGauss.set_in('SourceAlpha')
        self.myGauss.set_result('blur')
        self.addElement(self.myGauss)
        self.feColorMatrix = feColorMatrix()
        self.feColorMatrix.set_id('DropShadowColorMatrix')
        self.feColorMatrix.set_result('bluralpha')
        self.feColorMatrix.set_type('matrix')
        self.feColorMatrix.set_values('1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0.500000 0 ')
        self.addElement(self.feColorMatrix)
        self.feOffset = feOffset()
        self.feOffset.set_id('DropShadowOffset')
        self.feOffset.set_dx(1.0)
        self.feOffset.set_dy(1.0)
        self.feOffset.set_in('bluralpha')
        self.feOffset.set_result('offsetBlur')
        self.addElement(self.feOffset)
        self.feMerge = feMerge()
        self.feMerge.set_id('DropShadowMerge')
        self.addElement(self.feMerge)
        self.firstFeMergeNode = feMergeNode()
        self.feMerge.addElement(self.firstFeMergeNode)
        self.firstFeMergeNode.set_id('DropShadowMergeNode1')
        self.firstFeMergeNode.set_in('offsetBlur')
        self.secondFeMergeNode = feMergeNode()
        self.feMerge.addElement(self.secondFeMergeNode)
        self.secondFeMergeNode.set_id('DropShadowMergeNode2')
        self.secondFeMergeNode.set_in('SourceGraphic')


def Image():
    s = svg()
    i = image(x=80, y=25, width=88, height=31)
    i.set_xlink_href('http://img0.gmodules.com/ig/images/googlemail.gif')
    s.addElement(i)
    i = image(x=80, y=125, width=88, height=31)
    i.set_xlink_href('../sourceimages/images.jpg')
    s.addElement(i)
    print s.getXML()
    s.save('./testoutput/10_Image.svg')
    
      
def LinearGradient():
    mySVG = svg("test")
    d = defs()
  
    lg = linearGradient()
    lg.set_id("orange_red")
    s = stop(offset="0%")
    s.set_stop_color('rgb(255,255,0)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    s = stop(offset="100%")
    s.set_stop_color('rgb(255,0,0)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    d.addElement(lg)
  
    oh = ShapeBuilder()
    e = oh.createEllipse(cx="200", cy="190", rx="85", ry="55", fill="url(#orange_red)")
  
    mySVG.addElement(d)
    mySVG.addElement(e)
    print mySVG.getXML()
    mySVG.save('./testoutput/8_LinearGradient.svg')
 
def RadialGradient():
    mySVG = svg()
    d = defs()
   
    lg = radialGradient()
    lg.set_id("grey_blue")
    s = stop(offset='0%')
    s.set_stop_color('rgb(200,200,200)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    s = stop(offset='100%')
    s.set_stop_color('rgb(0,0,255)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    d.addElement(lg)
  
    oh = ShapeBuilder()
    e = oh.createEllipse(cx="230", cy="200", rx="110", ry="100", fill="url(#grey_blue)")
  
    mySVG.addElement(d)
    mySVG.addElement(e)
    print mySVG.getXML()
    mySVG.save('./testoutput/9_RadialGradient.svg')

def Grouping():
    s = svg()
  
    #testing container
    myStyle = StyleBuilder()
    myStyle.setStrokeWidth(2)
    myStyle.setStroke("green")

    group = g()
    group.set_style(myStyle.getStyle())
    group.addElement(line(300, 300, 600, 600))
    group.addElement(circle(500, 500, 50))
    s.addElement(group)
  
    group = g()
    group.set_style(myStyle.getStyle())
    style_dict = {"stroke":"#000000", "fill":"none" , "stroke-width":"49" , "stroke-opacity":"0.027276"}
    p = path(pathData="M 300 100 A 1,1 0 0 1 802,800")
    p.set_style(StyleBuilder(style_dict).getStyle())
    p2 = path(pathData="M 100 300 A 1,1 0 0 1 802,800")
    p2.set_style(StyleBuilder(style_dict).getStyle())
    group.addElement(p)
    group.addElement(p2)
    s.addElement(group)
    print s.getXML()
    s.save('./testoutput/7_Grouping.svg')


def ComplexShapes():
    oh=ShapeBuilder()
    mySVG=svg("test")
    d = defs()
    d.addElement(MyDropShadow())
    mySVG.addElement(d)

    pl=oh.createPolyline(points="50,375 150,375 150,325 250,325 250,375 350,375 350,250 450,250 450,375 \
550,375 550,175 650,175 650,375 750,375 750,100 850,100 850,375 950,375 \
950,25 1050,25 1050,375 1150,375 ",strokewidth=10, stroke='blue')
    mySVG.addElement(pl)
  
    pointsAsTuples=[(350,75),(379,161),(469,161),(397,215),(423,301),(350,250),(277,301),(303,215),(231,161),(321,161)]
    pg=oh.createPolygon(points=oh.convertTupleArrayToPoints(pointsAsTuples),strokewidth=10, stroke='blue', fill='red')
    pg.set_filter('url(#MyDropShadow)')
    mySVG.addElement(pg)
 
    sh=StyleBuilder()
    sh.setFilling('#EEE')
    sh.setStroke('#00F')
    sh.setStrokeWidth('2px')
    path1=path('M 40,530 L 100,560 L 60,520 Z', style=sh.getStyle())
    
    sh2=StyleBuilder()
    sh2.setFilling('#FFC')
    sh2.setStroke('#00F')
    sh2.setStrokeWidth('2px')
    path2=path(style=sh2.getStyle())
    path2.appendMoveToPath(190, 520, False)
    #as you can see we can mix strings and ints without trouble
    path2.appendCubicCurveToPath('+0', '+0', 30, 30, -60, 30, True)
    path2.appendCloseCurve()
  
    sh3=StyleBuilder()
    sh3.setFilling('none')
    sh3.setStroke('#00F')
    sh3.setStrokeWidth('2px')
    path3=path('M 230,530', style=sh3.getStyle())
    path3.appendQuadraticCurveToPath(0, 30, 30, 0)
    path3.appendQuadraticCurveToPath(30, -30, 30, 0)
    path3.appendQuadraticCurveToPath(-0, 30, 30, 0)
    path3.appendQuadraticCurveToPath(30, -20, 30, 0)
  
    mySVG.addElement(path1)
    mySVG.addElement(path2)
    mySVG.addElement(path3)
  
    mySVG.save('./testoutput/6_ComplexShapes.svg')


def Shapes():
    oh = ShapeBuilder()
    s = svg("test")
  
    s.addElement(oh.createRect(0, 0, 400, 200, 12, 12, strokewidth=2, stroke='navy'))
    s.addElement(oh.createRect(100, 50, 200, 100, strokewidth=2, stroke='navy', fill='yellow'))
    s.addElement(oh.createCircle(700, 500, 50, strokewidth=5, stroke='red'))
    s.addElement(oh.createCircle(810, 500, 50, strokewidth=5, stroke='yellow', fill='#AAAAAA'))
    s.addElement(oh.createEllipse(600, 50, 50, 30, strokewidth=5, stroke='red'))
    s.addElement(oh.createEllipse(700, 50, 50, 30, strokewidth=5, stroke='yellow', fill='#00AABB'))
    s.addElement(oh.createLine(0, 0, 300, 300, strokewidth=2, stroke="black"))
    s.save('./testoutput/4_Shapes.svg')
  
def Line():
    s = svg("test")
    myStyle = StyleBuilder()
    myStyle.setStrokeWidth(2)
    myStyle.setStroke('black')
    l = line(0, 0, 300, 300)
    l.set_style(myStyle.getStyle())
    s.addElement(l)
    #easier method with ShapeBuilder
    oh = ShapeBuilder()
    s.addElement(oh.createLine(10, 0, 300, 300, strokewidth=2, stroke="blue"))
    s.save('./testoutput/5_Line.svg')

def TextFeatures():
    s = svg("test")
    myStyle = StyleBuilder()
    myStyle.setFontFamily(fontfamily="Verdana")
    myStyle.setFontSize('5em')
    myStyle.setFilling(fill="blue")
    t1 = text("Verdana, blue, 5em", 0, 100)
    t1.set_style(myStyle.getStyle())
    t2 = text("pySVG simple", 0, 200)
    s.addElement(t1)
    s.addElement(t2)
  
    r = rect(350, 250, 100, 100, id="myRect")
    r.set_fill("green")
    s.addElement(r)
  
    myStyle = StyleBuilder()
    myStyle.setFontFamily(fontfamily="Times")
    myStyle.setFontSize('2em')
    myStyle.setFontStyle('italic')
    myStyle.setFontWeight('bold')
    myStyle.setFilling(fill="red")
    myStyle.setFillOpacity('0.5')
    myStyle.setFillRule('evenodd')
  
    t3 = text("Times, italic, 2em, bold, opacity=0.5, fillrule=evenodd", 0, 300)
    t3.set_style(myStyle.getStyle())
    s.addElement(t3)

    myStyle = StyleBuilder()
    myStyle.setFontFamily(fontfamily="Times")
    myStyle.setFontSize('2em')
    myStyle.setFontStyle('italic')
    myStyle.setFilling(fill="red")
    myStyle.setFillOpacity('0.5')
    #myStyle.fill="blue"
    t4 = text("Times, italic, 2em, non bold, opacity=0.5", 0, 400)
    t4.set_style(myStyle.getStyle())
    s.addElement(t4)

  
    print s.getXML()
    s.save('./testoutput/3_TextFeatures.svg')

def HelloWorld2():
    s = svg() 
    myStyle = StyleBuilder()
    myStyle.setFontFamily(fontfamily="Verdana")
    myStyle.setFontSize('5em') #no need for the keywords all the time
    myStyle.setFilling("blue")
    t1 = text("Hello World", 0, 100)
    t1.set_style(myStyle.getStyle())
    s.addElement(t1)
    print s.getXML()
    s.save('./testoutput/2_HelloWorld2.svg')

def HelloWorld1():
    s = svg()
    t = text("Hello World", 0, 100)
    s.addElement(t)
    print s.getXML()
    s.save('./testoutput/1_HelloWorld1.svg', encoding='UTF-8')

def KWARGS():
    s = svg() 
    kw={}
    kw['style']= 'font-size:20em; font-family:Verdana; fill:blue; '
    t1 = text("KWARGS Text", 0, 300, **kw)
    s.addElement(t1)
    print s.getXML()
    s.save('./testoutput/KWARGS.svg')


def tutorialChain():
    HelloWorld1()
    HelloWorld2()
    TextFeatures()
    Shapes()
    Line()
    ComplexShapes()
    Grouping()
    LinearGradient()
    RadialGradient()
    Image()
    KWARGS()
  
if __name__ == '__main__': 
    tutorialChain()
