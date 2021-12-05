from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import UserRequestSchema, UserResponseSchema,UserResponseWithArticleSchema
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/api/v1/user',
    tags=['user']
)


@router.post('', response_model=UserResponseSchema)
def create(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.create(db=db, request=request)


@router.get('/feed', response_model=List[UserResponseSchema])
def feed_initial_user(db: Session = Depends(get_db)):
    return db_user.db_feed(db)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all(db)


@router.get('/id/{user_id}', response_model= UserResponseWithArticleSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(user_id=user_id, db=db)