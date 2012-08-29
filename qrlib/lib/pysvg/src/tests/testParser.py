'''
Created on 26.05.2009

@author: kerim
'''

from pysvg import parser
from pysvg.structure import svg

def main():
    anSVG = parser.parse('./sourceimages/TMs10kSVGDemo.svg')
    anSVG.save('./testoutput/TMs10kSVGDemo.svg')
    
    anSVG = parser.parse('./sourceimages/clock.svg')
    anSVG.save('./testoutput/clock.svg')
    

if __name__ == "__main__":
    main()
