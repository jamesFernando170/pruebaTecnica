from ast import Str
from pydantic import BaseModel


class productBase(BaseModel):
    id: int
    name: Str
    description: Str
    price: int
    stock: int
    category_id: int


class productSchema(productBase):
    id: int

    class config:
        orm_mode = True


