from ast import Str
from enum import Enum
from typing import Union
from pydantic import BaseModel, EmailStr, Field


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'

class CreateUserRequest(BaseModel):
    username:str = Field(..., title="username for a user")
    full_name:str = Field(..., title="user's fullname ")
    email:EmailStr = Field(..., title="user's email address")
    password:str = Field(
        ...,
        min_length=8, 
        max_length=30, 
        title="authentication password for user")
    confirm_password:str = Field(
        ...,
        min_length=8, max_length=30,
        title="authentication password confirmation for user")


class UpdateUserRequest(BaseModel):
    username:Union[str,None] = Field(title="username for a user")
    email:Union[EmailStr,None] = Field(title="user's email address")
    full_name: Union[str,None] = Field(title="user's fullname ")
    gender : Union[Gender,None] = Field(title="user's gender ")

class UpdateUserPasswordRequest(BaseModel):
    confirmation_code:str = Field(..., min_length=8, max_length=30, title="password otp code")
    password:str = Field(..., min_length=8, max_length=30, title="authentication password for user")
    confirm_password:str = Field(..., min_length=8, max_length=30, title="authentication password confirmation for user")