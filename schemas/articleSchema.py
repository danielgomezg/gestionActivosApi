from typing import TypeVar, Optional
from pydantic import BaseModel
from datetime import date
from fastapi import UploadFile, File

T = TypeVar('T')

class ArticleSchema(BaseModel):
    name: str = None
    description: Optional[str] = None
    photo: str
    company_id: int = None

class ArticleEditSchema(BaseModel):
    name: str = None
    description: Optional[str] = None
    photo: Optional[str] = None
