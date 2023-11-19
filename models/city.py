#!/usr/bin/python3
'''
City class module
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    city class

    Attribute:
        state_id(str): contains id of state
        name(str): name of city
    '''
    state_id = ''
    name = ''
