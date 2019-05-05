from flask import Blueprint

# add your blueprints here, nothing more to do
from .main import main


# blueprints_list is used in app/init.py to register all blueprints
# blueprints_list is automatically filled :
blueprints_list = []
# list() is used cause globals change during the loop (blueprints_list will change)
for name, val in list(globals().items()):
    if isinstance(val, Blueprint):
        blueprints_list.append(val)
