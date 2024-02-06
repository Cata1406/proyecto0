from sqlalchemy.orm import Session
from src.services.user_service import get_user_by_id
from src.services.task_service import get_task_by_id
from src.models.user import User
from src.models.task import Task
from typing import List


def remove_task_from_user(db: Session, user_id: str, task_id: str) -> None:
    user: User = get_user_by_id(db, user_id)
    task: Task = get_task_by_id(db, task_id)
    user.tasks.remove(task)
    db.commit()
    db.refresh(user)
    return user

def remove_all_tasks_from_user(db: Session, user_id: str) -> None:
    user: User = get_user_by_id(db, user_id)
    user.tasks.clear()
    db.commit()
    db.refresh(user)
    return user

def get_tasks_by_user_id(db: Session, user_id: str) -> list:
    user: User = get_user_by_id(db, user_id)
    return user.tasks