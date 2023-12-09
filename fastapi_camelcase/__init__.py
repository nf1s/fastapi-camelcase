# -*- coding: utf-8 -*-
"""FastAPI CamelCase Parser Module

Module adds aliases to pydantic models
Module will decode the body and decamilize (camelCase => snake_case) its keys
then encode it back again.

example if the request.body = {"myVal":"Hello_world"},
the module will convert it to {"my_val":"Hello_world"}
and viceversa

"""
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

__author__ = "Ahmed Nafies <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies"
__license__ = "MIT"
__version__ = "2.0.0"


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
