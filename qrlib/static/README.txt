The style files concept is simple.

The module substitution algorithm iterates over the QR matrix and
checks the relative position of every module to it's neightboor modules.
The algorithm always assumes that the current processed module is located
in position 2b as in this matrix:

    a  b  c
  1
  2    x
  3

Al other positions are checked for active modules and the SVG style is
deduced. All current supported style files. Position is evaluated from
top to down, right to left:

   a  b  c
1                  This case represents a lone module "2b". 
2     x            
3

   a  b  c
1     x            This case represents "1b". From now on 2b is always omited
2     x            from the style code.
3
   a  b  c
1     x            This case represents "2a1b". 2b is always set so it's omited
2  x  x            from the style code.
3

   a  b  c
1     x             This case represents a lone module "1b3b". As always 
2     x             middle module is ommited as this is the current analysed
3     x             module and is always active.

TODO: Keep documenting
