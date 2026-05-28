

from fastapi import FastAPI

app = FastAPI()

#this was made just to show how api's are called.
@app.get("/")
def great():
    return {"message": "Welcome to Teluso Track"}

#to get all the products in the local host we made this function.
prodcuts=[
    {
        "id": 1,
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with USB receiver",
        "price": 15.99,
        "quantity": 25
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard with blue switches",
        "price": 49.99,
        "quantity": 12
    },
    {
        "id": 3,
        "name": "Gaming Headset",
        "description": "Surround sound headset with noise cancellation",
        "price": 35.50,
        "quantity": 18
    },
    {
        "id": 4,
        "name": "Laptop Stand",
        "description": "Adjustable aluminum laptop stand",
        "price": 22.75,
        "quantity": 30
    },
    {
        "id": 5,
        "name": "USB-C Hub",
        "description": "Multiport USB-C hub with HDMI support",
        "price": 27.40,
        "quantity": 20
    }
]

@app.get("/products")
def get_all_products():
    return prodcuts