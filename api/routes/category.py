# api/routes/category.py
from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.category_service import get_categories, create_category, update_category, delete_category
from models.category import Category

router = APIRouter()


@router.get("/", response_model=List[Category])
async def read_categories():
    return get_categories()


@router.post("/", response_model=Category, status_code=201)
async def add_category(category: Category):
    return create_category(category)


@router.put("/{category_id}", response_model=Category)
async def modify_category(category_id: str, category: Category):
    updated_category = update_category(category_id, category)
    if not updated_category:
        raise HTTPException(status_code=422, detail="Invalid category ID")
    return updated_category


@router.delete("/{category_id}", status_code=200)
async def remove_category(category_id: str):
    if not delete_category(category_id):
        raise HTTPException(status_code=404, detail="Category not found")
