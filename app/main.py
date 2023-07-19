from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body,Depends
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas
from .database import engine,get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app = FastAPI()






while True:

    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='yash1234',cursor_factory=RealDictCursor)
        print("Connection successful")
        cursor = conn.cursor()
        break

    except Exception as error:
        print("Unable to connect to database")
        print("error",error)
        time.sleep(2)



# def find_post(id):
#     for p in my_posts:
#         if p["id"]==id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p["id"]==id:
#             return i


@app.get("/")
def root():
    return {"message":"Hello World!!"}

@app.get("/posts",response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    #print(posts)
    return posts

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    # posts = cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[-1]
#     return {"detail":post}

@app.get("/posts/{id}",response_model=schemas.Post)
def get_post(id: int,response: Response, db: Session = Depends(get_db)):
    cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id),))
    post = cursor.fetchone()
    
    post = db.query(models.Post).filter(id==models.Post.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Post with {id} not found"}
    return post


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("DELETE FROM posts WHERE id = %s returning * ",(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(id==models.Post.id)

    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id = {id}")
    
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Post)
def update_post(id: int,updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id),))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(id==models.Post.id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id = {id}")
    
    post_query.update(updated_post.dict(),synchronize_session=False)

    db.commit()

    return post_query.first()
    



@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


