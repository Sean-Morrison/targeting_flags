# encoding: utf-8

from sdsstools import get_package_version
from .read import *

# pip package name
NAME = 'sdss-SDSS_targeting_flags'

# package name should be pip package name
__version__ = get_package_version(path=__file__, package_name=NAME)
SDSSC2BV = str(__version__).split('.')[0]
