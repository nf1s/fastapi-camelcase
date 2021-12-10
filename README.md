[![CircleCI](https://circleci.com/gh/nf1s/fastapi-camelcase.svg?style=shield)](https://circleci.com/gh/nf1s/fastapi-camelcase) [![codecov](https://codecov.io/gh/nf1s/fastapi-camelcase/branch/master/graph/badge.svg)](https://codecov.io/gh/nf1s/fastapi-camelcase) [![Downloads](https://pepy.tech/badge/fastapi-camelcase)](https://pepy.tech/project/fastapi-camelcase) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/nf1s/fastapi-camelcase) ![GitHub](https://img.shields.io/github/license/nf1s/fastapi-camelcase)

# Fastapi Camelcase

Package for providing a class for camelizing request and response bodies for fastapi
while keeping your python code snake cased.

Full documentation can be found [here](https://nf1s.github.io/fastapi-camelcase/)

## How to install

```bash
pip install fastapi-camelcase
```

## Dependencies

    pydantic
    pyhumps

## How to use

```python
# using CamelModel instead of Pydantic BaseModel
from fastapi_camelcase import CamelModel


class User(CamelModel):
    first_name: str
    last_name: str
    age: int
```

## How to use (full example)

```python
import uvicorn
from fastapi import FastAPI
from fastapi_camelcase import CamelModel


class User(CamelModel):
    first_name: str
    last_name: str
    age: int


app = FastAPI()


@app.get("/user/get", response_model=User)
async def get_user():
    return User(first_name="John", last_name="Doe", age=30)


@app.post("/user/create", response_model=User)
async def create_user(user: User):
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
