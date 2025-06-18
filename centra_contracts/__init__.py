from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = True
