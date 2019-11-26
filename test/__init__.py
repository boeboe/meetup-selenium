"""Package with tests """
from os.path import dirname, basename, isfile
import glob
import meetup_selenium

MODULES = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in MODULES if isfile(f) and not f.endswith('__init__.py')]
