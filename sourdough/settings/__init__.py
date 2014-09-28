# Start off by loading base settings.
from .base import *

# Override base settings with local settings.
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(['{0} (did you rename settings/local-dist.py?)'.format(exc.args[0])])
    raise exc
