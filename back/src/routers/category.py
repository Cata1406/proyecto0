from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.category import CategoryRead, CategoryCreate, CategoryUpdate
from src.schemas.task import TaskRead
import src.services.category_service as service
import src.services.category_task_service as category_task_service
import src.services.task_service as task_service
from src.config.db_config import get_db
from fastapi_jwt_auth import AuthJWT
from src.services.authentication_service import authorized_user_id, authorized_admin_user
from fastapi.security import HTTPAuthorizationCredentials
from fastapi_jwt_auth import AuthJWT
from src.routers.user import get_bearer_token

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[CategoryRead], status_code=200)
def get_all_categories(db: Session = Depends(get_db),token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    #authorized_user_id(db, Authorize)
    return service.get_all_categories(db)


@router.get("/{category_id}", response_model=CategoryRead, status_code=200)
def get_category_by_id(category_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    #authorized_admin_user(db, Authorize)
    return service.get_category_by_id(db, category_id)


@router.get("/{category_id}/tasks", response_model=List[TaskRead], status_code=200)
def get_tasks_by_category_id(category_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    db_category = service.get_category_by_id(db, category_id)
    return category_task_service.get_tasks_by_category_id(db, category_id)


@router.post("/", response_model=CategoryRead, status_code=201)
def create_category(category: CategoryCreate = Body(...), db: Session = Depends(get_db),token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    service.get_category_by_name(db, category.name)
    return service.create_category(db, category)


@router.put("/{category_id}", response_model=CategoryRead, status_code=200)
def update_category(category_id: str, category: CategoryUpdate = Body(...), db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    db_category = service.get_category_by_id(db, category_id)
    return service.update_category(db, db_category, category)


@router.delete("/{category_id}", response_model=None, status_code=204)
def delete_category(category_id: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    #authorized_admin_user(db, Authorize)
    db_category = service.get_category_by_id(db, category_id)
    category_task_service.remove_all_tasks_from_category(db, category_id)
    service.delete_category(db, category_id)


@router.delete("/", response_model=None, status_code=204)
def delete_all_categories(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials | None = Depends(get_bearer_token), Authorize: AuthJWT = Depends()):
    authorized_admin_user(db, Authorize)
    db_categories = service.get_all_categories(db)
    task_service.delete_all_tasks(db)
    service.delete_all_categories(db)
