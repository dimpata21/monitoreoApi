from typing import Optional
from pydantic import BaseModel
import datetime

#se crea el modelo
class Monitoreo(BaseModel):
    _id: Optional[str]
    lugar: str
    autor: str
    temperatura: float
    humedad: float
    createdAt: Optional[datetime.datetime]
    updatedAt: Optional[datetime.datetime]
