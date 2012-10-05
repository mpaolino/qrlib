# coding: utf-8
# (c) Copyright 2012 by Miguel Paolino <mpaolino@ideal.com.uy>

class StyleFileMissing(Exception):
    pass

class StyleMissing(Exception):
    pass

class InnerEyeStyleMissing(StyleMissing):
    pass

class OuterEyeStyleMissing(StyleMissing):
    pass

class InvalidColor(Exception):
    pass

class InvalidSize(Exception):
    pass

class InvalidLanguage(Exception):
    pass

class InvalidAppSize(Exception):
    pass

class InvalidApplication(Exception):
    pass

class InvalidEcLevel(Exception):
    pass
