#!/usr/bin/python3
"""Class definition for the file storage
   type for the AirBnB_v2 project
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """Defining a class that will  serialize the  instances
    to JSON file type and deserializes JSON file to instances
    Attrib:
        __file_path: The path to JSON file
        __objects: The objects that will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Function that will return a dictionary
        Return:
            dict of __object
        """
        dicti = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dicti[key] = self.__objects[key]
            return (dicti)
        else:
            return self.__objects

    def new(self, obj):
        """Fuunction to set __object to a given object
        Arguments
            obj: The given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Function that will serialize file path to JSON file path
        """
        my_dicti = {}
        for key, value in self.__objects.items():
            my_dicti[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dicti, f)

    def reload(self):
        """Function that will serialize file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Function that will delete existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
