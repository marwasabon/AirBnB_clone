#!/usr/bin/python3

from models.base_model import BaseModel
from console import HBNBCommand
import unittest
from unittest.mock import patch
from console import HBNBCommand
from unittest import TestCase
from io import StringIO


class TestConsole(TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_missing_class_name(self):
        result = self.console.onecmd('create')
        self.assertEqual(result, '** class name missing **')

    def test_create_class_doesnt_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create MyModel')
            self.assertEqual(f.getvalue().strip(), '** class doesn\'t exist **')

    def test_show_missing_class_name(self):
        result = self.console.onecmd('show')
        self.assertEqual(result, '** class name missing **')

    def test_show_class_doesnt_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('show MyModel')
            self.assertEqual(f.getvalue().strip(), '** class doesn\'t exist **')

    def test_show_missing_instance_id(self):
        result = self.console.onecmd('show BaseModel')
        self.assertEqual(result, '** instance id missing **')

    def test_show_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('show BaseModel 121212')
            self.assertEqual(f.getvalue().strip(), '** no instance found **')

    def test_destroy_missing_class_name(self):
        result = self.console.onecmd('destroy')
        self.assertEqual(result, '** class name missing **')

    def test_destroy_class_doesnt_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('destroy MyModel')
            self.assertEqual(f.getvalue().strip(), '** class doesn\'t exist **')

    def test_destroy_missing_instance_id(self):
        result = self.console.onecmd('destroy BaseModel')
        self.assertEqual(result, '** instance id missing **')

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('destroy BaseModel 121212')
            self.assertEqual(f.getvalue().strip(), '** no instance found **')

    def test_update_missing_class_name(self):
        result = self.console.onecmd('update')
        self.assertEqual(result, '** class name missing **')

    def test_update_class_doesnt_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update MyModel')
            self.assertEqual(f.getvalue().strip(), '** class doesn\'t exist **')

    def test_update_missing_instance_id(self):
        result = self.console.onecmd('update BaseModel')
        self.assertEqual(result, '** instance id missing **')

    def test_update_missing_attribute_name(self):
        result = self.console.onecmd('update BaseModel existing-id')
        self.assertEqual(result, '** attribute name missing **')

    def test_update_missing_value_for_attribute(self):
        result = self.console.onecmd('update BaseModel existing-id first_name')
        self.assertEqual(result, '** value missing **')



if __name__ == "__main__":
    unittest.main()
