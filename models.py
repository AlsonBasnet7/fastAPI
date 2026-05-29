
# What is a Model?
# A model is basically a blueprint for data.
# It defines:
# what data exists,
# what type it is,
# and how it should be stored in the database.
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

