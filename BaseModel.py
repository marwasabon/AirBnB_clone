import uuid
import unittest
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

# Testing the BaseModel class
 
class TestBaseModel(unittest.TestCase):
    def test_init(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
    def test_str(self):
        base_model = BaseModel()
        self.assertEqual(str(base_model), "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__))
        
    def test_save(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)
        
    def test_to_dict(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], base_model.updated_at.isoformat())

if __name__ == "main":
    unittest.main()
