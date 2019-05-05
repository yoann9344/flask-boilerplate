# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies

# You must import all of the new Models you create to this page
from .Email import Email
from .Person import Person
from .base import db

# __all__ = ["Email", "Person", "db"]
# __all__ is automatically filled :
__all__ = []
# list() is used cause globals change during the loop (__all__ change)
for name, val in list(globals().items()):
    # if the the first character is not a _ then it is not a special variable/method
    if name[0] != '_':
        __all__.append(name)
