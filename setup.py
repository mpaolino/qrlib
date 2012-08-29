import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "qrlib",
    version = "0.0.1",
    author = "Miguel Paolino",
    author_email = "mpaolino@ideal.com.uy",
    description = ("QR generation library"),
    license = "Propietary",
    keywords = "qr library qrlib ideal",
    url = "http://github.com/mpaolino/qrlib",
    packages=['qrlib', 'qrlib.lib', 'qrlib.fonts', 'qrlib.static'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        ],
    package_dir={'qrlib': 'qrlib'},
    package_data={'qrlib': ['static/*.png', 'fonts/*.ttf']},
    install_requires=['PIP>=1.1.7']
    )
