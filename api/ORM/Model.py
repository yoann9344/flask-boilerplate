# for more detail, see class Model in :
# https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/model.py
from typing import Any, List, Type


class ModelSQL(object):
    query_class = None  # flask_alchemy attribute
    query = None  # flask_alchemy attribute

    DONOTSEND_MODEL = {'_sa_instance_state'}
    DONOTSEND = []

    def __repr__(self) -> str:
        return '<{}>'.format(self.__class__.__name__)

    def to_dict_recursive(self) -> dict:
        return self._to_dict_recursive(obj_ids_crossed=[id(self)])

    def _to_dict_recursive(self, obj_ids_crossed: List[int]) -> dict:
        # functions :
        # anti_circular_recursion : check if we've already called the object
        #                               if not do the recursion
        # type_shunt_recursive : select the actions for each type of attr

        def check_crossed(obj: Type[ModelSQL]) -> any:
            if id(obj) in obj_ids_crossed:
                return str(obj)
                # others possibilities
                # return str(obj).join(' ').join(str(obj.id))
                # return obj.id
            else:
                obj_ids_crossed.append(id(obj))
                return obj._to_dict_recursive(obj_ids_crossed)

        ##### what about dict which contains object(s) ? Is it possible in SQLAlchemy ?
        def type_shunt_recursive(attribute: Any) -> Any:
            # model
            if issubclass(type(attribute), ModelSQL):
                return anti_circular_recursion(attribute)
            # recursive iteration of the list in case of the list is a relationship
            elif isinstance(attribute, list):
                values = []
                for item in attribute:
                    values.append(type_shunt_recursive(item))
                return values
            # attribute is not an instance of relationship (int, str..)
            else:
                return attribute

        result = {}
        # __mapper__ is equivalent to db.inspect(self)
        # but db (database) is not created yet cause we send this model to the constructor
        for key in self.__mapper__.attrs.keys():
            if key not in self.DONOTSEND:
                attr = getattr(self, key)
                result[key] = type_shunt_recursive(attr)

        return result
