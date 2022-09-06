from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    id:Union(str)
    username:str
    email:str
    password:str


router = APIRouter(
    prefix="/documents",
    tags= ["documents"],
    dependencies=[]
)

@router.post("/uploads")
async def get_profile(user_id:str):
    pass

@router.put("/uploads")
async def get_profile(user_id:str):
    pass
