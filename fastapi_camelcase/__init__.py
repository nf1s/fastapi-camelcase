# -*- coding: utf-8 -*-
"""FastAPI CamelCase Parser Module

Module adds aliases to pydantic models 
Module will decode the body and decamilize (camelCase => snake_case) its keys
then encode it back again.

example if the request.body = {"myVal":"Hello_world"},
the module will convert it to {"my_val":"Hello_world"}
and viceversa

"""
from humps import camelize
from pydantic import BaseModel

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "1.0.0"


class CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
