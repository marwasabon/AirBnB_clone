#!/usr/bin/python3
'''A command line intepreter
This module contains a command line interpreter
'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    '''Command interpreter class
    contains simple command for CRUD operations

    Attr:
        prompt(str): prompt string
    '''
    class_dict = {
        "BaseModel": 'BaseModel',
        "User": 'User'
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
            if len(my_list) == 1:
                print(self.class_dict[my_list[0]])
                obj = eval("{}()".format(self.class_dict[my_list[0]]))
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
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if len(my_list) < 2:
                raise SyntaxError()
            objects = storage.all()
            key = "{}.{}".format(self.class_dict[my_list[0]], my_list[1])
            print(objects[key])
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
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
        my_list = []
        try:
            if not line:
                raise SyntaxError()
            if line not in self.all_classes:
                raise NameError()
            objects = storage.all(self.all_classes[line])
            for key in objects:
                my_list.append(objects[key])
            print(my_list)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

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
            args = line.split(" ")
            if args[0] not in self.all_classes:
                raise NameError()
            objects = storage.all(self.all_classes[args[0]])
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                raise KeyError()
            if len(args) < 3:
                raise SyntaxError()
            if len(args) < 4:
                raise SyntaxError()
            if len(args) < 5:
                raise SyntaxError()
            if len(args) > 5:
                raise SyntaxError()
            obj = objects[key]
            setattr(obj, args[2], args[3])
            storage.save()
        except SyntaxError:
            print("** attribute name missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
