"""Package to model meetup entities """
from os.path import dirname, basename, isfile

__version__ = '0.0.1'

import glob
MODULES = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in MODULES if isfile(f) and not f.endswith('__init__.py')]
