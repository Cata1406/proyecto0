from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum
from sqlalchemy.orm import relationship
from src.config.db_config import Base
import enum

class TaskState(enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True)
    text = Column(String)
    creation_date = Column(DateTime)
    forseen_end_date = Column(DateTime)
    state = Column(Enum(TaskState), default=TaskState.TODO)

    user_id = Column(String, ForeignKey("users.id"))
    category_id = Column(String, ForeignKey("categories.id"))

    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")