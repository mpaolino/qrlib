

def getExtremum(items, function, operator):
    i = 0
    current = items[i]
    extremum = function(current)
    while i < len(items) - 1:
        i += 1
        current = items[i]
        if operator(function(current), extremum):
            extremum = function(current)
    return extremum
    

class Line(BaseElement):
    
    @classmethod
    def from_points(cls, start, end, style_dict=None,focusable=None):
        return cls(start[0], start[1], end[0], end[1], style_dict, focusable)


class Rectangle(BaseElement):
        
    def show_inner_box(self, show_box):
        if show_box:
            self.create_inner_box()
            self.getXML = self.getXML_with_inner
        else:
            self.getXML = BaseElement.getXML
            
    def create_inner_box(self):
        self.inner_box.elements = []
        edges = self.get_inner_edge_points()
        self.inner_box.addElement(Line.from_points(edges[0], edges[1]))
        self.inner_box.addElement(Line.from_points(edges[1], edges[2]))
        self.inner_box.addElement(Line.from_points(edges[2], edges[3]))
        self.inner_box.addElement(Line.from_points(edges[3], edges[0]))
        
        
    def getXML_with_inner(self):
        myXML = BaseElement.getXML(self)
        myXML += self.inner_box.getXML()
        return myXML

    
    def transform_to_include(self, elements):
        self.x = getExtremum([e.get_bottom_left()[0] for e in elements], lambda p:p, lambda n,c: n < c)
        self.y = getExtremum([e.get_bottom_left()[1] for e in elements], lambda p:p, lambda n,c: n < c)
        self.x -= self.rx
        self.y -= self.ry
        most_right = getExtremum([e.get_top_right()[0] for e in elements], lambda p:p, lambda n,c: n > c)
        most_top = getExtremum([e.get_top_right()[1] for e in elements], lambda p:p, lambda n,c: n > c)
        self.width = most_right + self.rx - self.x
        self.height = most_top + self.ry - self.y
        




class PolyLine(polyline):

    def getWidth(self):
        xs = [p[0] for p in self.points]
        max_x = xs.pop()
        min_x = max_x
        while len(xs) > 0:
            current = xs.pop()
            if current > max_x:
                max_x = current
            if current < min_x:
                min_x = current
        return abs(max_x - min_x)

    def getHeight(self):
        ys = [p[1] for p in self.points]
        max_y = ys.pop()
        min_y = max_y
        while len(ys) > 0:
            current = ys.pop()
            if current > max_y:
                max_y = current
            if current < min_y:
                min_y = current
        return abs(max_y - min_y)

    def get_bottom_left(self):
        x = getExtremum([p[0] for p in self.points], lambda p:p, lambda n,c: n < c)
        y = getExtremum([p[1] for p in self.points], lambda p:p, lambda n,c: n < c)
        return (x,y)




class Shape(SVG):

    anchor_points = {}
    zero = (0,0)

    def __init__(self, *args, **kwargs):
        SVG.__init__(self,*args, **kwargs)

    def getXML(self, full = True):
        if full:
            xml=SVG_HEADER
        else:
            xml = ""
        if self.height!= None:
            xml += 'height="%s" ' % (self.height)
        if self.width!= None:
            xml += 'width="%s" ' % (self.width)
        if self.viewBox!= None:
            xml += 'viewBox="%s" ' % (self.viewBox)
        xml += END_TAG_LINE
        for element in self.elements:
            xml += element.getXML()
        if full:
            xml += SVG_FOOTER
        return xml

    def getWidt(self):
        i = 0
        current = self.elements[i]
        max = current.getWidth()
        while i < len(self.elements) - 1:
            i += 1
            current = self.elements[i]
            if current.getWidth() > max:
                max = current.getWidth()
        return max

    def getHeight(self):
        i = 0
        current = self.elements[i]
        max = current.getHeight()
        while i < len(self.elements) - 1:
            i += 1
            current = self.elements[i]
            if current.getHeight() > max:
                max = current.getWidth()
        return max

    def centerToPoint(self, shape, point):
        pass

    def addNormalized(self, element):
        element.normalize_to_point(self.zero)
        self.addElement(element)


