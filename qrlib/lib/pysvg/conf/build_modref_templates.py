#!/usr/bin/env python
"""Script to auto-generate our API docs.
"""
# stdlib imports
import os, sys

# local imports
from apigen import ApiDocWriter

#*****************************************************************************
if __name__ == '__main__':
    sys.path.append(os.path.abspath('../src'))
    package = 'pysvg'
    outdir = os.path.join('','generated')
    docwriter = ApiDocWriter(package)
    #docwriter.package_skip_patterns += [r'\.fixes$',
    #                                    r'\.externals$',
    #                                    r'\.neurospin\.viz',
    #                                    ]
    docwriter.write_api_docs(outdir)
    docwriter.write_index(outdir, 'gen', relative_to='api')
    print '%d files written' % len(docwriter.written_modules)
