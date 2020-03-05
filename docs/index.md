[![CircleCI](https://circleci.com/gh/ahmednafies/fastapi_camelcase.svg?style=shield)](https://circleci.com/gh/ahmednafies/fastapi_camelcase) ![](./coverage.svg)
# fastapi_camelcase
Package for providing a class for camelizing request and response bodies for fastapi
while keeping your python code snake cased.

## How to install
    pip install fastapi-camelcase

## Dependencies 
    pydantic

## How to use
    # using CamelModel instead of Pydantic BaseModel
    from fastapi_camelcase import CamelModel


    class User(CamelModel):
        first_name: str
        last_name: str
        age: int

