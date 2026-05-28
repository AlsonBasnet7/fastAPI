

from fastapi import FastAPI

app = FastAPI()

def great():
    return {"message": "Welcome to Teluso Track"}
