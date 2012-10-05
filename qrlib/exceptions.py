# coding: utf-8
# (c) Copyright 2012 by Miguel Paolino <mpaolino@ideal.com.uy>

class StyleFileMissing(Exception):
    def __init__(self, style, filename):
        if not isinstance(filename, (str, unicode)) or \
            not isinstance(style, (str, unicode)):
            raise AttributeError
        self.style = style
        self.filename = filename

    def __repr__(self):
        return 'Style \'%s\' misses file \'%s\'' % (self.filepath)


class StyleMissing(Exception):
    def __init__(self, style):
        if not isinstance(style, (str, unicode)):
            raise AttributeError
        self.style = style

    def __repr__(self):
        return 'Style \'%s\' is missing' % (self.style)
