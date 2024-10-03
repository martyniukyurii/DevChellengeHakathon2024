# services/category_service.py

from models.category import Category, default_categories
from typing import List, Optional

categories_db = default_categories.copy()  # Simulating a database with default categories


def get_categories() -> List[Category]:
    return categories_db


def create_category(category: Category) -> Category:
    categories_db.append(category)
    return category


def update_category(category_id: str, category_data: Category) -> Optional[Category]:
    for category in categories_db:
        if category.id == category_id:
            category.title = category_data.title or category.title
            category.points = category_data.points or category.points
            return category
    return None


def delete_category(category_id: str) -> bool:
    global categories_db
    categories_db = [category for category in categories_db if category.id != category_id]
    return True
