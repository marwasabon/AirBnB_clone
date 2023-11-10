#!/usr/bin/python3
'''A command line intepreter
This module contains a command line interpreter
'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class
    contains simple command for CRUD operations

    Attr:
        prompt(str): prompt string
    '''
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
            NameError: when there is no object taht has the name
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if len(my_list) == 1:
                obj = eval("{}()".format(my_list[0]))
            else:
                kwargs = HBNBCommand.parse_line(my_list[1:])
                obj = eval("{}(**{})".format(my_list[0], kwargs))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()
