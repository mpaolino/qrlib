#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pysvg.structure import *
from pysvg.builders import *
from pysvg.gradient import pattern

#actions not working
def createText(content, x,y, actions=None):
  t=text(content,x,y)
  return t

def createMainBorderAndTexts():
  oh=ShapeBuilder()
  sh=StyleBuilder()
  elements=[]
  r=oh.createRect("0", "0", "946", "626", strokewidth="2px", stroke="#00C", fill="#FFF")
  elements.append(r)
  sh.setFilling("#000")
  sh.setFontSize("24px")
  t=text("Objects and Effects in ...", 30, 40)
  t.set_style(sh.getStyle())
  elements.append(t)
  sh=StyleBuilder()
  sh.setFontSize("13px")
  t=text("[The red circle, explanation texts and textlinks WILL (but are not yet) connected to JavaScript.]", 360, 35)
  t.set_style(sh.getStyle())
  elements.append(t)
  
  elements.append(createText("Rectangle",230,90))
  elements.append(createText("Circle",230,180))
  elements.append(createText("Ellipse",230,275))
  elements.append(createText("Polygon",100,350))
  elements.append(createText("Polyline",270,350))
  elements.append(createText("Line",270,470))
  elements.append(createText("Path",190,570))
  elements.append(createText("flowing Text",800,550))
  elements.append(createText("linear gradient",600,90))
  elements.append(createText("radial gradient",600,170))
  elements.append(createText("opacity",600,310))
  elements.append(createText("filter",600,440))
  elements.append(createText("animation",800,375))
  
  elements.append(createText("pattern",600,550))
  elements.append(createText("group + transformation",780,190))
  elements.append(createText("external Picture",800,310))
  elements.append(createText("Textlink",800,495))
  
  return elements
  """
  <!--### Hauptrahmen und Textinhalte ###-->

k  <rect x="0" y="0" width="946" height="626" style="fill: #FFF; stroke: #00C; stroke-width: 2px"/>
no-tspan with onmouse...  <text x="30" y="40" style="fill: #000; font-size: 24px">Objekte und Effekte in <tspan style="fill: #F00" onmouseover="InfoText('&lt;svg width=&quot;...&quot; height=&quot;...&quot;&gt;SVG-Dokument&lt;/svg&gt;','v')" onmouseout="InfoText('','h')">SVG</tspan></text>

k  <text x="360" y="35" style="fill: #000; font-size: 13px">[Der rote Kreis, die Erklärungstexte und die Textlinks sind mit JavaScript-Funktionen verknüpft.]</text>
nok  <a xlink:href="mailto:thomas@handmadecode.de"><text id="mail" class="klein" x="5" y="620" onmouseover="TextHover('mail','#F00','underline')" onmouseout="TextHover('mail','#00C','none')">&#169; by Dr. Thomas Meinike 2002</text></a>
nok  <text x="830" y="620" class="klein">TMs10kSVGDemo.svg</text>

nok  <text id="info" x="0" y="620" style="fill: #000; visibility: hidden">Text</text>
  <text x="230" y="90"  onmouseover="InfoText('&lt;rect x=&quot;...&quot; y=&quot;...&quot; width=&quot;...&quot; height=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Rechteck</text>

  <text x="230" y="180" onmouseover="InfoText('&lt;circle cx=&quot;...&quot; cy=&quot;...&quot; r=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Kreis</text>
  <text x="230" y="275" onmouseover="InfoText('&lt;ellipse cx=&quot;...&quot; cy=&quot;...&quot; rx=&quot;...&quot; ry=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Ellipse</text>
  <text x="100" y="350" onmouseover="InfoText('&lt;polygon points=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Polygon</text>
  <text x="270" y="350" onmouseover="InfoText('&lt;polyline points=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Polylinie</text>
  <text x="270" y="470" onmouseover="InfoText('&lt;line x1=&quot;...&quot; y1=&quot;...&quot; x2=&quot;...&quot; y2=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Linie</text>
  <text x="190" y="570" onmouseover="InfoText('&lt;path d=&quot;...&quot; style=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">Pfad</text>

  <text x="800" y="550" onmouseover="InfoText('&lt;text x=&quot;...&quot; y=&quot;...&quot; style=&quot;...&quot;&gt;...&lt;/text&gt;','v')" onmouseout="InfoText('','h')">normaler Fließtext</text>
  <text x="600" y="90"  onmouseover="InfoText('&lt;linearGradient&gt;&lt;stop offset=&quot;...&quot; style=&quot;...&quot;/&gt;&lt;/linearGradient&gt;','v')" onmouseout="InfoText('','h')">linearer Gradient</text>
  <text x="600" y="170" onmouseover="InfoText('&lt;radialGradient&gt;&lt;stop offset=&quot;...&quot; style=&quot;...&quot;/&gt;&lt;/radialGradient&gt;','v')" onmouseout="InfoText('','h')">radialer Gradient</text>
  <text x="600" y="310" onmouseover="InfoText('style=&quot;fill-opacity: ...; stroke-opacity: ...&quot;','v')" onmouseout="InfoText('','h')">Opazität (Durchlässigkeit)</text>
  <text x="600" y="440" onmouseover="InfoText('&lt;filter&gt;&lt;feFiltername ... /&gt;&lt;/filter&gt;','v')" onmouseout="InfoText('','h')">Spezialfilter</text>
  <text x="800" y="375" onmouseover="InfoText('&lt;objekt ...&gt;&lt;animate ... /&gt;&lt;/objekt&gt;','v')" onmouseout="InfoText('','h')">Animation</text>

  <text x="600" y="550" onmouseover="InfoText('&lt;pattern&gt;&lt;fuellobjekt ... style=&quot;...&quot;/&gt;&lt;/pattern&gt;','v')" onmouseout="InfoText('','h')">Muster</text>
  <text x="780" y="190" onmouseover="InfoText('&lt;g transform=&quot;rotate(...)&quot;&gt;&lt;objekt ... /&gt;...&lt;/g&gt;','v')" onmouseout="InfoText('','h')">Gruppe+Transformation</text>
  <text x="800" y="310" onmouseover="InfoText('&lt;image xlink:href=&quot;...&quot; x=&quot;...&quot; y=&quot;...&quot; width=&quot;...&quot; height=&quot;...&quot;/&gt;','v')" onmouseout="InfoText('','h')">externes Bild</text>
  <text x="800" y="495" onmouseover="InfoText('&lt;a xlink:href=&quot;...&quot;&gt;&lt;text x=&quot;...&quot; y=&quot;...&quot; style=&quot;...&quot;&gt;...&lt;/text&gt;&lt;/a&gt;','v')" onmouseout="InfoText('','h')">Textlink</text>
  """
def createShapes():
  oh=ShapeBuilder()
  sh=StyleBuilder()
  elements=[]
  #rectangles
  r=oh.createRect(30, 70, 80, 30, strokewidth='0',fill='#090')
  elements.append(r)
  r=oh.createRect(120, 70, 80, 30, strokewidth='2px', stroke='#00C', fill='#FFC')
  elements.append(r)
  
  #circles
  c=oh.createCircle(60, 170, 30, strokewidth='0',fill='#F00')
  #<circle id="kreis1" cx="60" cy="170" r="30" style="fill: #F00" onmouseover="FillHover('kreis1','#FF0','#00C','5px')" onmouseout="FillHover('kreis1','#F00','none','0px')"/>
  elements.append(c)
  c=oh.createCircle(150, 170, 30, strokewidth='2px', stroke='#000', fill='#FF0')
  elements.append(c)
 
  #ellipse
  e=oh.createEllipse(60, 270, 30, 15, strokewidth='0',fill='#F00')
  #<circle id="kreis1" cx="60" cy="170" r="30" style="fill: #F00" onmouseover="FillHover('kreis1','#FF0','#00C','5px')" onmouseout="FillHover('kreis1','#F00','none','0px')"/>
  elements.append(e)
  e=oh.createEllipse(150, 270, 30, 15, strokewidth='2px', stroke='#000', fill='#CCC')
  elements.append(e)
  
  #polygon
  p=oh.createPolygon('60,370, 70,360, 80,400, 50,440, 40,330', strokewidth='2px', stroke='#000', fill='#FFF')
  elements.append(p)

  #line
  l=oh.createLine(60,470,180,470, strokewidth='2px', stroke='#00C')
  elements.append(l)
  l=oh.createLine(200,470,260,400, strokewidth='2px', stroke='#F00')
  elements.append(l)
  
  #path
  p=createPaths()
  for e in p:
    elements.append(e)
  
  #polyline
  p=oh.createPolyline('250,325 200,345 250,365', strokewidth='2px', stroke='#090')
  elements.append(p)

  #opacity
  sh=StyleBuilder()
  sh.setFilling('#00C')
  sh.setFillOpacity(0.5)
  c=circle(450, 290, 50)
  c.set_style(sh.getStyle())
  elements.append(c)
  sh=StyleBuilder()
  sh.setFilling('#00C')
  sh.setFillOpacity(0.2)
  sh.setStroke('#00C')
  sh.setStrokeOpacity(0.3)
  c=circle(475, 325, 50)
  c.set_style(sh.getStyle())
  elements.append(c)
  
  #group + transform
  th=TransformBuilder()
  th.setRotation('-30')
  group=g()
  group.set_transform(th.getTransform())
  r=oh.createRect(620, 500, width='100', height='50', rx=10, ry=10, stroke='#F00',strokewidth='2px',fill='none')
  group.addElement(r)
  
  sh=StyleBuilder()
  sh.setFilling('none')
  sh.setFontSize('36px')
  sh.setStrokeWidth('1px')
  sh.setStroke('#00C')
  t=text('Text',635, 537)
  t.set_style(sh.getStyle())
  group.addElement(t)
  elements.append(group)
  
  
  return elements

  
def createPaths():
  elements=[]
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
  elements.append(path1)
  elements.append(path2)
  elements.append(path3)
  return elements
"""
  <!-- Gradienten -->
  <rect x="400" y="70" width="180" height="30" style="fill: url(#lingra1)"/>
  <circle cx="450" cy="170" r="50" style="fill: url(#radgra1)"/>
  <!-- Filter -->

  <circle cx="450" cy="440" r="50" style="fill: #090; filter: url(#filter1)"/>
"""  
def getLinearGradient():
    lg=linearGradient();
    lg.set_id('lingra1')
    stop1=stop('0%')
    stop2=stop('50%')
    stop3=stop('100%')
    stop1.set_style("stop-color: #000")
    stop2.set_style("stop-color: #00F")
    stop3.set_style("stop-color: #FFF")
    lg.addElement(stop1)
    lg.addElement(stop2)
    lg.addElement(stop3)
    return lg

def getRadialGradient():
    rg=radialGradient();
    rg.set_id('radgra1')
    stop1=stop('0%')
    stop2=stop('60%')
    stop3=stop('100%')
    stop1.set_style("stop-color: #FFF")
    stop2.set_style("stop-color: #FF9")
    stop3.set_style("stop-color: #F00")
    rg.addElement(stop1)
    rg.addElement(stop2)
    rg.addElement(stop3)
    return rg
    
"""
   <!-- Animation -->
  <rect x="600" y="360" width="0" height="20" style="fill: #F00; fill-opacity: 0.6">
    <animate attributeType="XML" attributeName="width" begin="0s" dur="10s" fill="freeze" from="0" to="180"/>
  </rect>
"""
def createImageAndLink():
    """
    <!-- externes Bild -->
    <image x="800" y="250" xlink:href="bilder/adobesvg.gif" width="88" height="31"/> 

    <!-- Textlink -->
    <a xlink:href="http://www.datenverdrahten.de" target="_top"><text id="textlink" x="600" y="495" style="fill: #F00" onmouseover="TextHover('textlink','#00C','underline')" onmouseout="TextHover('textlink','#F00','none')">http://www.datenverdrahten.de</text></a>
    """
    elements=[]
    myImage=image(800, 250, 88, 31)
    myImage.set_xlink_href('http://www.google.de/intl/de_de/images/logo.gif')
    elements.append(myImage)
    
    myHyperlink = a('_top')
    myHyperlink.set_xlink_href('http://codeboje.de/pysvg')
    linkText=text('http://codeboje.de/pysvg', 600, 495)
    linkText.set_id='textlink'
    linkText.set_style('fill: #F00')
    myHyperlink.addElement(linkText)
    elements.append(myHyperlink)
    return elements

def createDefs():
    d = defs()
    
    """
    <pattern id="muster1" height="20" width="20" patternUnits="userSpaceOnUse" y="0" x="0"  >
    <rect style="fill: #00C" height="10" width="10" y="0" x="0"  />
    </pattern>
    """
  
    p = pattern(0,0,20,20,"userSpaceOnUse")
    p.set_id("muster1")
    
    r = rect(0, 0, 10, 10)
    r.set_style("fill: #00C")
    p.addElement(r)
    d.addElement(p)
    return d
   

def createPattern():
    """
    <!--  Muster  -->
    <rect style="fill: url(#muster1)" height="50" width="150" y="520" x="400"  />
    """
    r = rect(400, 520, 150, 50)
    r.set_style("fill: url(#muster1)")
    return r
  
    
def main():
  s=svg(height="100%", width="100%")
  s.set_viewBox("0 0 950 630")
  s.addElement(createDefs())
  for element in createMainBorderAndTexts():
    s.addElement(element)
  for element in createShapes():
    s.addElement(element)
  for element in createImageAndLink():
    s.addElement(element)
  s.addElement(createPattern())
  print s.getXML()
  s.save('./testoutput/testDefaultpySVGScreen.svg')
if __name__ == '__main__': 
  main()