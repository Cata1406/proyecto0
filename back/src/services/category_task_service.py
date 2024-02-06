from sqlalchemy.orm import Session
from src.services.category_service import get_category_by_id
from src.services.task_service import get_task_by_id
from src.models.category import Category
from src.models.task import Task


#def assign_task_to_category(db: Session, category_id: str, task_id: str) -> None:
    #category: Category = get_category_by_id(db, category_id)
    #task: Task = get_task_by_id(db, task_id)
    #category.tasks.append(task)
    #db.commit()
    #db.refresh(category)
    #return category

def remove_task_from_category(db: Session, category_id: str, task_id: str) -> None:
    category: Category = get_category_by_id(db, category_id)
    task: Task = get_task_by_id(db, task_id)
    category.tasks.remove(task)
    db.commit()
    db.refresh(category)
    return category

def remove_all_tasks_from_category(db: Session, category_id: str) -> None:
    category: Category = get_category_by_id(db, category_id)
    category.tasks.clear()
    db.commit()
    db.refresh(category)
    return category

def get_tasks_by_category_id(db: Session, category_id: str) -> list:
    category: Category = get_category_by_id(db, category_id)
    return category.tasks