from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel

class Transaction(BaseModel):
    id:Union(str)
    username:str
    email:str
    password:str


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)



@router.get("/{id}")
async def get_transaction_by_id(id:str):
    pass

@router.get("/")
async def get_transaction_by_id(query):
    pass

@router.post("/")
async def get_transaction_by_id(transaction:Transaction):
    pass
