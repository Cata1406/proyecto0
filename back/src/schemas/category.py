from pydantic import BaseModel
from typing import List
from src.schemas.task import TaskRead

class CategoryBase(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Work",
                "description": "Work related tasks"
            }
        }

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: str
    tasks: List[TaskRead]
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c",
                "name": "Work",
                "description": "Work related tasks",
                "tasks": [
                    {
                        "id": "4f21a77d-b8fa-47bb-8df6-b772a635bc19",
                        "text": "Do the dishes",
                        "creation_date": "2021-06-01",
                        "forseen_end_date": "2021-06-02",
                        "state": "STARTED",
                        "user_id": "60e3b2be-b29d-442c-b5ea-6337d0044a9e",
                        "category_id": "ce53abbe-d973-4033-b38b-1d20e6e5a98c"
                    }
                ]
            }
        }
    

class CategoryUpdate(BaseModel):
    name: str | None
    description: str | None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Work",
                "description": "Work related tasks"
            }
        }
