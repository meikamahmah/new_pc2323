import fastapi
import uvicorn
from uvicorn import run

print("Hello")
api = fastapi.FastAPI()


@api.get("/")
def endpoint():
    return {"msg": "Hello Hello"}


run(api)
