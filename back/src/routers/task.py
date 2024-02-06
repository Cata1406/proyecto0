from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.task import TaskRead, TaskCreate, TaskUpdate
import src.services.task_service as service
from src.config.db_config import get_db
from src.routers.user import get_bearer_token
from fastapi_jwt_auth import AuthJWT
from fastapi.security import HTTPAuthorizationCredentials
from src.services.authentication_service import authorized_user_id, authorized_admin_user


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[TaskRead], status_code=200)
def get_all_tasks(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    return service.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskRead, status_code=200)
def get_task_by_id(task_id: str, db: Session = Depends(get_db),token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    task = service.get_task_by_id(db, task_id)
    user_id = task.user_id
    authorized_user_id(db, Authorize, user_id)
    return task


@router.post("/", response_model=TaskRead, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    user_id = task.user_id
    authorized_user_id(db, Authorize, user_id)
    return service.create_task(db, task)


@router.put("/{task_id}", response_model=TaskRead, status_code=200)
def update_task(task_id: str, task: TaskUpdate, db: Session = Depends(get_db),token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    db_task = service.get_task_by_id(db, task_id)
    authorized_user_id(db, Authorize, db_task.user_id)
    return service.update_task(db, db_task, task)


@router.delete("/{task_id}", response_model=None, status_code=204)
def delete_task(task_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    db_task = service.get_task_by_id(db, task_id)
    authorized_user_id(db, Authorize, db_task.user_id)
    service.delete_task(db, task_id)


@router.delete("/", response_model=None, status_code=204)
def delete_all_tasks(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    db_tasks = service.get_all_tasks(db)
    service.delete_all_tasks(db)