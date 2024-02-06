from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.config.db_config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    profile_picture = Column(String, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fes.m.wikipedia.org%2Fwiki%2FArchivo%3ADefault_pfp.svg&psig=AOvVaw1CL6O0VOcMV50tHBkOq0v2&ust=1707259752909000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKD4w6qklYQDFQAAAAAdAAAAABAf")
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan", passive_deletes=True)

