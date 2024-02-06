from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from src.schemas.user import UserRead, UserCreate, UserUpdate, UserBase
from src.schemas.task import TaskRead
import src.services.user_service as service
import src.services.user_task_service as user_task_service
import src.services.task_service as task_service
#import src.services.category_service as category_service
from src.config.db_config import get_db
from fastapi_jwt_auth import AuthJWT
#from fastapi_versioning import VersionedFastAPI, version
from src.services.authentication_service import authorized_user_id, authorized_admin_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"detail": "Not found"}},
)

get_bearer_token = HTTPBearer(auto_error=False)

@router.get("/", response_model=List[UserRead], status_code=200)
def get_all_users(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    return service.get_all_users(db)


@router.get("/{user_id}", response_model=UserRead, status_code=200)
def get_user_by_id(user_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_user_id(db, Authorize, user_id)
    return service.get_user_by_id(db, user_id)     


@router.get("/{user_id}/tasks", response_model=List[TaskRead], status_code=200)
def get_tasks_by_user_id(user_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_user_id(db, Authorize, user_id)
    return user_task_service.get_tasks_by_user_id(db, user_id)


@router.post("/", response_model=UserUpdate, status_code=201)
def create_user(user: UserCreate = Body(...), db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.post("/login", status_code=201)
def login_user(user: UserBase = Body(...), Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    db_user = service.get_user_by_username(db, user.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    access_token = Authorize.create_access_token(subject=db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}


@router.put("/{user_id}", response_model=UserRead, status_code=200)
def update_user(user_id: str, user: UserUpdate = Body(...), db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_user_id(db, Authorize, user_id)
    db_user = service.get_user_by_id(db, user_id)
    return service.update_user(db, db_user, user)


@router.delete("/{user_id}", response_model=None, status_code=204)
def delete_user(user_id: str, db: Session = Depends(get_db),token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_user_id(db, Authorize, user_id)
    db_user = service.get_user_by_id(db, user_id)
    user_task_service.remove_all_tasks_from_user(db, user_id)
    service.delete_user(db, user_id)


@router.delete("/", response_model=None, status_code=204)
def delete_all_users(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    db_users = service.get_all_users(db)
    task_service.delete_all_tasks(db) 
    service.delete_all_users(db)