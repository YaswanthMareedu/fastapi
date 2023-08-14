
from .. import models,schemas,utils
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body,Depends
from ..database import engine,get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)

    check = db.query(models.User).filter(user.email==models.User.email).first()
    if check:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"User Already Exists")
    print('Visited')
    posts = db.query(models.Post).all()
    print(posts)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with: {id} does not exist")
    
    return user