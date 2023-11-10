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
                print("** class name missing **")
            else:
                if my_list[0] not in classes:
                    print("** class doesn't exist **")
                else:
                    kwargs = {}
                    for arg in my_list[1:]:
                        if "=" in arg:
                            key_value = arg.split("=")
                            key = key_value[0]
                            value = key_value[1].replace('"', '')
                            kwargs[key] = value
                    obj = eval("{}(**{})".format(my_list[0], kwargs))
                    obj.save()
                    print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
