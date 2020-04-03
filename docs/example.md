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
