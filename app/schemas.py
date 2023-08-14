from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title:str
    content:str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at:datetime
    owner_id: int
    owner: UserOut
    

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None



class Vote(BaseModel):
    post_id: int
    dir: int





