from pydantic import BaseModel, Field
from typing import Optional, Tuple


class Supplier(BaseModel):
    supplierID:int
    supplierName:str

class Product(BaseModel):
    productID:int
    prodname:str
    price:int
    supp:Supplier

class Customer(BaseModel):
    custID:int
    custname:str
    prod:Tuple[Product]