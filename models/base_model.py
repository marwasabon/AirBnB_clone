#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    def __init__(self):
        """Instantiation of base model class
            Args:
                args: it won't be used
                kwargs: arguments for the constructor of the BaseModel
            Attributes:
                id: unique id generated
                created_at: creation date
                updated_at: updated date
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
        returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
            """return a string representaion
            """
            return self.__str__()
    
    def save(self):
        """updates the public instance attribute updated_at to current
        """
    
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
        returns a dictionary of all the key values in __dict__
        """
    
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
