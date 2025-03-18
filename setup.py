import sys
from setuptools import setup

# Check Python version: require 2.7 or >= 3.4
if sys.version_info[:2] < (2, 7) or (3, 0) <= sys.version_info[:2] < (3, 4):
    sys.exit("Python version 2.7 or >= 3.4 required.")

setup()  # Reads configuration from setup.cfg