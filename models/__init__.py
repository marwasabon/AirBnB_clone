#!/usr/bin/python3
'''
Contains package initialization directives
'''
from engine import file_storage as fs


storage = fs.FileStorage()
storage.reload()
