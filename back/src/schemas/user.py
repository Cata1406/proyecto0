from pydantic import BaseModel
from typing import List
from src.schemas.task import TaskRead

class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "john123"
            }
        }


class UserCreate(UserBase):
    profile_picture: str | None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "john123",
                "profile_picture": "https://www.google.com"
            }
        }

class UserRead(UserBase):
    id: str
    tasks: List[TaskRead]
    profile_picture: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "60e3b2be-b29d-442c-b5ea-6337d0044a9e",
                "username": "johndoe",
                "password": "john123",
                "profile_picture": "https://www.google.com",
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
    
    

class UserUpdate(BaseModel):
    username: str | None
    password: str | None
    profile_picture: str | None
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "john123",
                "profile_picture": "https://www.google.com"
            }
        }