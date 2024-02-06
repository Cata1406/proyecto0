from uuid import uuid4
from sqlalchemy.orm import Session
from src.models.user import User as UserModel
from src.schemas.user import UserCreate, UserRead, UserUpdate
from src.models.task import Task as TaskModel
from typing import List
from fastapi import HTTPException


def get_all_users(db: Session) -> List[UserModel]:
    users = db.query(UserModel).all()
    users_found(users)
    return users


def get_user_by_id(db: Session, user_id: str) -> UserModel:
    user_id_provided(user_id)
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    user_found(user)
    return user


def get_user_by_username(db: Session, username: str) -> UserModel:
    user = db.query(UserModel).filter(UserModel.username == username).first()
    return user


def create_user(db: Session, user: UserCreate) -> UserUpdate:

    username_provided(user.username)
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=409, detail ="Username already exists")
    
    password_provided(user.password)
    
    new_user = UserModel(
        id=str(uuid4()),
        username=user.username,
        password=user.password,
        profile_picture=user.profile_picture
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: UserRead, user_to_update: UserUpdate) -> UserModel:

    if user_to_update.username:
        if get_user_by_username(db, user_to_update.username):
            raise HTTPException(status_code=409, detail ="Username already exists")
        user.username = user_to_update.username
    
    if user_to_update.password:
        user.password = user_to_update.password

    if user_to_update.profile_picture:
        user.profile_picture = user_to_update.profile_picture
    
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: str) -> UserModel:
    user_to_delete = db.query(UserModel).filter(UserModel.id == user_id).first()
    db.delete(user_to_delete)
    db.commit()


def delete_all_users(db: Session) -> None:
    db.query(UserModel).delete()
    db.commit()


# Helper functions
def user_id_provided(user_id: str):
    if not user_id:
        raise HTTPException(status_code=404, detail="User id must be provided")

def username_provided(username: str):
    if not username:
        raise HTTPException(status_code=404, detail="Username must be provided")

def password_provided(password: str):
    if not password:
        raise HTTPException(status_code=404, detail="Password must be provided")
    
def users_found(users: List[UserModel]):
    if not users:
        raise HTTPException(status_code=404, detail="No users found")

def user_found(user: UserModel):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")