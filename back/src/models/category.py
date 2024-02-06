from sqlalchemy import Column, ForeignKey, String, Integer, Date
from sqlalchemy.orm import relationship
from src.config.db_config import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    tasks = relationship("Task", back_populates="category", cascade="all, delete-orphan", passive_deletes=True)