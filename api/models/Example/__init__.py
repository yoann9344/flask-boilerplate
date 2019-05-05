# import there all classes, no more to do
from .Album import Album
from .Image import Image

# __all__ is automatically filled :
__all__ = []
# list() is used cause globals change during the loop (__all__ change)
for name, val in list(globals().items()):
    # if the the first character is not _ then it is not a special variable/method
    if name[0] != '_':
        __all__.append(name)
