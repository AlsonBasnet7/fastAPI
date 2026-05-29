

from fastapi import FastAPI
from pydantic import BaseModel
from models import Product
from database import session

app = FastAPI()

#this was made just to show how api's are called.
@app.get("/")
def great():
    return {"message": "Welcome to Teluso Track"}

#to get all the products in the local host we made this function.
products = [
    Product(id=1, name="Wireless Mouse", description="Ergonomic wireless mouse with USB receiver", price=15.99, quantity=25),
    Product(id=2, name="Mechanical Keyboard", description="RGB mechanical keyboard with blue switches", price=49.99, quantity=12),
    Product(id=3, name="Gaming Headset", description="Surround sound headset with noise cancellation", price=35.50, quantity=18),
    Product(id=4, name="Laptop Stand", description="Adjustable aluminum laptop stand", price=22.75, quantity=30),
    Product(id=5, name="USB-C Hub", description="Multiport USB-C hub with HDMI support", price=27.40, quantity=20)
]

#returns all the products stored in the products.
@app.get("/products")
def get_all_products():
    #we will be connecting the database here
    #query
    db = session()
    db.query()
    return products

#this reads the product via id
@app.get("/products/{product_id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return {"message": "Product not found"} 

#this will create the new product.
@app.post("/product")
def add_products(product: Product):
    products.append(product)
    return products

#this will update the new product.
@app.put("/product")
def update_product(id: int, product: Product):

    for i in range(len(products)):

        if products[i].id == id:
            products[i] = product
            return "Product updated successfully!"

    return "No products found!"

#this will delete the new data/products from the system.
@app.delete("/products/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Prodcut is Deleted!"
        
    return "Product not found!"