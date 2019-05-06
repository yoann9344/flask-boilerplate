from flask_sqlalchemy import SQLAlchemy
from .Model import ModelSQL


db = SQLAlchemy(model_class=ModelSQL)
