# models/category.py

from pydantic import BaseModel, Field
from typing import List
import uuid


class Category(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    points: List[str]


# Predefined categories
default_categories = [
    Category(title="Visa and Passport Services", points=["Border crossing", "International documentation"]),
    Category(title="Diplomatic Inquiries", points=["Visa policies", "Embassy contacts"]),
    Category(title="Travel Advisories", points=["Travel restrictions", "Health alerts"]),
    Category(title="Consular Assistance", points=["Emergency contacts", "Legal advice"]),
    Category(title="Trade and Economic Cooperation", points=["Trade agreements", "Business opportunities"]),
]
