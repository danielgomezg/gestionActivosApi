from typing import TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class SucursalSchema(BaseModel):
    description: str
    number: str = None
    address: str
    region: str = None
    city: str = None
    commune: str = None
    company_id: int

class SucursalEditSchema(BaseModel):
    description: str
    number: str
    address: str

