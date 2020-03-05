[![CircleCI](https://circleci.com/gh/ahmednafies/fastapi_camelcase.svg?style=shield)](https://circleci.com/gh/ahmednafies/fastapi_camelcase) ![](./coverage.svg)
# fastapi_camelcase
Package for providing a class for camelizing request and response bodies for fastapi
while keeping your python code snake cased.

Full code can be found on [github](https://github.com/ahmednafies/fastapi_camelcase)

## Dependencies 
    pydantic
    pyhumps

## Usage
    # using CamelModel instead of Pydantic BaseModel
    from fastapi_camelcase import CamelModel


    class User(CamelModel):
        first_name: str
        last_name: str
        age: int

