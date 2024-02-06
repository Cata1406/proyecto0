from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Session
from src.models.task import Task as TaskModel
from src.schemas.task import TaskCreate, TaskRead, TaskUpdate
from src.services.user_service import get_user_by_id
from src.services.category_service import get_category_by_id
from pytz import utc
from typing import List
from fastapi import HTTPException
from src.models.task import TaskState


def get_all_tasks(db: Session) -> List[TaskModel]:
    tasks =  db.query(TaskModel).all()
    tasks_found(tasks)
    return tasks


def get_task_by_id(db: Session, task_id: str) -> TaskModel:
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    task_found(task)
    return task


def create_task(db: Session, task: TaskCreate) -> TaskModel:
    
    if not task.text:
        raise HTTPException(status_code= 404, detail="Text must be provided")
    
    if not task.forseen_end_date:
        raise HTTPException(status_code = 404, detail = "Forseen end date must be provided")
    now = datetime.now(utc)
    is_valid_date(now, task.forseen_end_date)

    if not task.user_id:
        raise HTTPException(status_code= 404, detail="User id must be provided")
    if not get_user_by_id(db, task.user_id):
        raise HTTPException(status_code= 404, detail="User id does not exist")

    if not task.category_id:
        raise HTTPException(status_code=404, detail="Category id must be provided")
    category_found(db, task.category_id)
    
    new_task = TaskModel(
        id=str(uuid4()),
        text=task.text,
        creation_date=now,
        forseen_end_date=task.forseen_end_date,
        user_id=task.user_id,
        category_id=task.category_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, task: TaskRead, task_to_update: TaskUpdate) -> TaskModel:
    
    if task_to_update.text:
        task.text = task_to_update.text

    if task_to_update.forseen_end_date:
        is_valid_date(task.creation_date, task_to_update.forseen_end_date)
        task.forseen_end_date = task_to_update.forseen_end_date
        
    if task_to_update.state:
        #if task_to_update.state != TaskState.TODO and task_to_update.state != TaskState.IN_PROGRESS and task_to_update.state != TaskState.DONE:
        if task_to_update.state != "TODO" and task_to_update.state != "IN_PROGRESS" and task_to_update.state != "DONE":
            raise HTTPException(status_code=400, detail="State must be TODO, IN_PROGRESS or DONE")
        task.state = task_to_update.state
    
    if task_to_update.category_id:
        category_found(db, task_to_update.category_id)
        task.category_id = task_to_update.category_id
    
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: str) -> TaskModel:
    task_to_delete = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    db.delete(task_to_delete)
    db.commit()
    return task_to_delete


def delete_all_tasks(db: Session) -> None:
    db.query(TaskModel).delete()
    db.commit()

## Helper functions
    
def category_found(db, category_id) -> bool:
    if not get_category_by_id(db, category_id):
        raise HTTPException(status_code=404, detail="Category id does not exist")


def tasks_found(tasks: List[TaskModel]) -> bool:
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")


def task_found(task: TaskModel) -> bool:
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")


def is_valid_date(creation_date: datetime, forseen_end_date: datetime) -> bool:
    if creation_date > forseen_end_date:
        raise HTTPException(status_code = 400, detail = "Forseen end date must be after creation date")
  

    