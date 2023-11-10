#!/usr/bin/python3
'''
Contains package initialization directives
'''
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
