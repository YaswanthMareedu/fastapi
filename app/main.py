from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine,get_db
from .routers import post,user,auth,vote


#models.Base.metadata.create_all(bind=engine)
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# def find_post(id):
#     for p in my_posts:
#         if p["id"]==id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p["id"]==id:
#             return i
print('Main visited')
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"Welcome to Multiverse, Lets Connect Together.."}






