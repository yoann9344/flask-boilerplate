from flask_sqlalchemy import SQLAlchemy
from backend.models.Model import ModelSQL


db = SQLAlchemy(model_class=ModelSQL)
