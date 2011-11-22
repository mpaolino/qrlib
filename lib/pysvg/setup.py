#!/usr/bin/env python

from distutils.core import setup

setup(name="pysvg",
      version="0.2.1",
      description="Python SVG Library",
      author="Kerim Mansour",
      author_email="kmansour@web.de",
      url="http://codeboje.de/pysvg/",
      packages=['pysvg'],
      package_dir={"pysvg":"src/pysvg"},
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics',
          ],
     )
