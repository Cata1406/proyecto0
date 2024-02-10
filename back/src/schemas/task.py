from pydantic import BaseModel
from datetime import datetime
from src.models.task import TaskState
from typing import Optional

class TaskBase(BaseModel):
    text: str
    forseen_end_date: datetime
    user_id: str
    category_id: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "text": "Do the dishes",
                "forseen_end_date": "2024-06-02T17:23:52.30Z",
                "user_id": "60e3b2be-b29d-442c-b5ea-6337d0044a9e",
                "category_id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c"
            }
        }

class TaskCreate(TaskBase):
    state: Optional[str]
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "text": "Do the dishes",
                "forseen_end_date": "2024-06-02T17:23:52.30Z",
                "state": "IN_PROGRESS",
                "user_id": "60e3b2be-b29d-442c-b5ea-6337d0044a9e",
                "category_id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c"
            }
        }

class TaskRead(TaskBase):
    creation_date: datetime
    id: str
    state: TaskState
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "4f21a77d-b8fa-47bb-8df6-b772a635bc19",
                "text": "Do the dishes",
                "creation_date": "2021-06-02T17:23:52.30Z",
                "forseen_end_date": "2024-06-02T17:23:52.30Z",
                "state": "IN_PROGRESS",
                "user_id": "60e3b2be-b29d-442c-b5ea-6337d0044a9e",
                "category_id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c"
            }
        }


class TaskUpdate(BaseModel):
    state: Optional[str]
    text: Optional[str]
    forseen_end_date: Optional[datetime]
    category_id : Optional[str]
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "text": "Do the dishes",
                "forseen_end_date": "2024-06-02T17:23:52.30Z",
                "state": "IN_PROGRESS",
                "category_id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c"
            }
        }
