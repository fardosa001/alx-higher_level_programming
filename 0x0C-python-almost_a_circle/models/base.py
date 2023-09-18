#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes Base class
        Args:
            id(int): id

        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))
        filename = cls.__name__ + ".json"
            
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1,1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        obj_list = []

        try:
            with open(filename, 'r') as f:
                instances = cls.from_json_string(f.read())
                for obj in instances:
                    obj_list.append(cls.create(**obj))
        except Exception:
            pass

        return obj_list
