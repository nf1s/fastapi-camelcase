# FastAPI Camelcase

[![CircleCI](https://circleci.com/gh/ahmednafies/fastapi_camelcase.svg?style=shield)](https://circleci.com/gh/ahmednafies/fastapi_camelcase) [![codecov](https://codecov.io/gh/ahmednafies/fastapi_camelcase/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/fastapi_camelcase) [![Downloads](https://pepy.tech/badge/fastapi-camelcase)](https://pepy.tech/project/fastapi-camelcase) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ahmednafies/fastapi_camelcase) ![GitHub](https://img.shields.io/github/license/ahmednafies/fastapi_camelcase)

Package for providing a class for camelizing request and response bodies for fastapi
while keeping your python code snake cased.

Full code can be found on [github](https://github.com/ahmednafies/fastapi_camelcase)

## Dependencies

    pydantic
    pyhumps

## Usage

```python
# using CamelModel instead of Pydantic BaseModel
from fastapi_camelcase import CamelModel


class User(CamelModel):
    first_name: str
    last_name: str
    age: int
```
