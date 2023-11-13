import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
import sys
import os


class TestConsole(unittest.TestCase):
    '''Test for console module'''

    def setUp(self):
        '''Set up the test'''
        self.console = HBNBCommand()

    def tearDown(self):
        '''Clean up the test'''
        del self.console

    def test_create(self):
        '''Test the create method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as:
            self.console.onecmd("create BaseModel")
            self.assertTrue(str(storage.all().values()) != "")

    def test_show(self):
        '''Test the show method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 12345-123")
            self.assertTrue(f.read() == "** no instance found **\n")

    def test_all(self):
        '''Test the all method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue(f.read() == "[]\n")

    def test_update(self):
        '''Test the update method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345-123")
            self.assertTrue(f.read() == "** no instance found **\n")

    def test_destroy(self):
        '''Test the destroy method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 12345-123")
            self.assertTrue(f.read() == "** no instance found **\n")

    def test_quit(self):
        '''Test the quit method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit") == True)

    def test_EOF(self):
        '''Test the EOF method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF") == True)

    def test_empty_line(self):
        '''Test the empty line method'''
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd(" ") == None)

