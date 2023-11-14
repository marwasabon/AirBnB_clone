#!/usr/bin/python3
'''A command line intepreter
This module contains a command line interpreter
'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class
    contains simple command for CRUD operations

    Attr:
        prompt(str): prompt string
    '''
    class_dict = {
            "BaseModel": 'BaseModel',
            "User": 'User',
            "State": State, "City": City,
            "Amenity": Amenity,
            "Place": Place, "Review": Review

    }

    prompt = "(hbnb) "

    def do_EOF(self, line):
        '''EOF command to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return self.do_EOF(line)

    def emptyline(self):
        '''Handle when empty line is passed'''
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.class_dict:
                raise NameError()
            if len(my_list) == 1:
                obj = eval("{}()".format(my_list[0]))
            else:
                kwargs = HBNBCommand.parse_line(my_list[1:])
                obj = eval("{}(**{})".format(class_dict[my_list[0]], kwargs))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """shows/prints  all the instances in string representation
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            my_list = line.split()
            if not my_list:
                raise SyntaxError()
            class_name = my_list[0]
            obj_id = my_list[1]

            class_dict = storage.class_dict
            if class_name not in class_dict:
                raise NameError()

            objects = storage.all()

            key = "{}.{}".format(class_name, obj_id)
            if key not in objects:
                raise KeyError
            print(objects[key])
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

        except IndexError:
            print("** instance id missing **")

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if len(my_list) < 2:
                raise SyntaxError()
            objects = storage.all()
            key = "{}.{}".format(self.class_dict[my_list[0]], my_list[1])
            del objects[key]
            storage.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
            """
        objects = storage.all()
        if line:
            class_name = line.split(" ")[0]
            if class_name not in self.class_dict:
                print("** class doesn't exist **")
                return
            objects = {
                key: value
                for key, value in objects.items()
                if value.__class__.__name__ == class_name
            }
        my_list = [str(value) for value in objects.values()]
        print(my_list)

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            args = line.split()
            if args[0] not in self.class_dict:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                raise KeyError()
            obj = objects[key]
            if len(args) < 3:
                raise AttributeError()
            if len(args) < 4:
                raise ValueError()
            obj = objects[key]

            setattr(obj, args[2], args[3])
            storage.save()
        except SyntaxError:
            print("** class name missing **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_count(self, line):
        """count the number of instances of a class
        """
        counter = 0
        try:
            my_list = split(" ")
            if my_list[0] not in self.class_dict:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
