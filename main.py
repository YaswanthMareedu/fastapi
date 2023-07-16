from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"Salaar","content":"Movie","id":1}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p


@app.get("/")
def root():
    return {"message":"Hello World!!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"]=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"posts":my_posts}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[-1]
#     return {"detail":post}

@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Post with {id} not found"}
    return {"post details":post}

