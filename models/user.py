#!/usr/bin/python3
'''
User module
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    User class

    Attribute:
        email(str): user email
        password(str): user password
        first_name(str): user first_name
        last_name(str): user last_name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
