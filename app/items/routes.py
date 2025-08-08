from fastapi import APIRouter, Depends
from dependencies import Dependency
from .schemas import Customer, Product 


router = APIRouter()


@router.get("/items/")
async def read_items(dep: Dependency = Depends(Dependency)):
    return {"message": "This is the items route."}



@router.post('/invoice')
async def getInvoice(c1: Customer):
    return c1
