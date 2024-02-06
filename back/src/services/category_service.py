from uuid import uuid4
from sqlalchemy.orm import Session
from src.models.category import Category as CategoryModel
from src.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from typing import List
from fastapi import HTTPException


def get_all_categories(db: Session) -> List[CategoryModel]:
    categories = db.query(CategoryModel).all()
    categories_found(categories)
    return categories


def get_category_by_id(db: Session, category_id: str) -> CategoryModel:
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    category_found(category)
    return category


def get_category_by_name(db: Session, category_name: str) -> CategoryModel:
    category = db.query(CategoryModel).filter(CategoryModel.name == category_name).first()
    if category:
        raise HTTPException(status_code=409, detail="Category already exists")
   


def get_categories_by_user_id(db: Session, user_id: str) -> List[CategoryModel]:
    return db.query(CategoryModel).filter(CategoryModel.user_id == user_id).all()


def create_category(db: Session, category: CategoryCreate) -> CategoryModel:

    category_name_provided(category.name)
    category_description_provided(category.description)

    new_category = CategoryModel(
        id=str(uuid4()),
        name=category.name,
        description=category.description
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def update_category(db: Session, category: CategoryRead, category_to_update: CategoryUpdate) -> CategoryModel:

    if category_to_update.name:
        get_category_by_name(db, category_to_update.name)
        category.name = category_to_update.name
    
    if category_to_update.description:
        category.description = category_to_update.description
        
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: str) -> None:
    category_to_delete = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    db.delete(category_to_delete)
    db.commit()


def delete_all_categories(db: Session) -> None:
    db.query(CategoryModel).delete()
    db.commit()

# Helper functions
def categories_found(categories: List[CategoryModel]) -> None:
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    
def category_found(category: CategoryModel) -> None:
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
def category_name_provided(category_name: str) -> None:
    if not category_name:
        raise HTTPException(status_code=400, detail="Category name is required")
    
def category_description_provided(category_description: str) -> None:
    if not category_description:
        raise HTTPException(status_code=400, detail="Category description is required")
    