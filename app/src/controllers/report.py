from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    id:Union(str)
    username:str
    email:str
    password:str


router = APIRouter(
    prefix="/reports",
    tags= ["reports"],
    dependencies=[]
)

@router.get("/generate")
async def get_profile(user_id:str):
    pass

@router.get("/generate/{user_id}")
async def get_user_by_id(user_id:str):
    pass

@router.delete("/{user_id}")
async def delete_user(user_id:str):
    pass
