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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
