import imp
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from .upload import document
class User(BaseModel):
    id:Union(str)
    username:str
    email:str
    password:str


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

router.include_router(document.router)

@router.get("/me")
async def get_profile(user_id:str):
    pass

@router.put("/me")
async def update_user_profile(user_id:str):
    pass


@router.get("/{user_id}")
async def get_user_by_id(user_id:str):
    pass

@router.put("/{user_id}")
async def update_user_by_id(user_id:str):
    pass

@router.post("/")
async def create_user(payload:User):
    pass


@router.delete("/{user_id}")
async def delete_user(user_id:str):
    pass


