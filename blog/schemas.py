from typing import List, Union
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

# extend blobase class


class Blog(BlogBase):

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    creator: ShowUser

    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str  # using username not email because jwt requires the identifier as username | usando nombre de usuario, no correo electrónico porque jwt requiere el identificador como nombre de usuario
    password: str


# for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None