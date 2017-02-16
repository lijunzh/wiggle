#!/usr/bin/env python
"""Wiggle Plot for Seismic Data Section

Visualize seismic data section using wiggle plots.
"""

DOCLINES = __doc__.split("\n")

import sys

from setuptools import setup, find_packages

# Check Python version
if sys.version_info[:2] < (2, 7) or (3, 0) <= sys.version_info[0:2] < (3, 4):
    raise RuntimeError("Python version 2.7 or >= 3.4 required.")

CLASSIFIERS = """\
Development Status :: 2 - Pre-Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS

"""

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)


# VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

def setup_package():
    # Figure out whether to add ``*_requires = ['numpy']``.
    # We don't want to do that unconditionally, because we risk updating
    # an installed numpy which fails too often.  Just if it's not installed, we
    # may give it a try.  See gh-3379.
    try:
        import numpy
    except ImportError:  # We do not have numpy installed
        build_requires = ['numpy>=1.8.2']
    else:
        # If we're building a wheel, assume there already exist numpy wheels
        # for this platform, so it is safe to add numpy to build requirements.
        # See gh-5184.
        build_requires = (['numpy>=1.8.2'] if 'bdist_wheel' in sys.argv[1:]
                          else [])

    try:
        import matplotlib
    except ImportError:
        build_requires += ['matplotlib>=2.0.0']

    metadata = dict(
        name='wiggle',
        maintainer="Lijun Zhu",
        version=VERSION,
        maintainer_email="gatechzhu@gmail.com",
        description=DOCLINES[0],
        long_description="\n".join(DOCLINES[2:]),
        url="https://github.com/gatechzhu/wiggle",
        download_url="https://github.com/gatechzhu/wiggle/releases",
        license='MIT',
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
        test_suite='tests',
        packages=find_packages(),
        setup_requires=build_requires,
        install_requires=build_requires,
        tests_require=build_requires + ['pytest'],
    )

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
