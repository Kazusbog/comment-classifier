from pydantic import BaseModel, Field
from typing import Optional

class SourceBase(BaseModel): #тут описана схема валидации данных для модели Source
    name:str = Field(..., min_length=1, description="Название источника не может быть пустым")
    description:Optional[str] = None

class SourceCreate(SourceBase): #при создании источника, мы можем передать только имя и описание
    pass

class SourceResponse(SourceBase): #при ответе на запрос, мы возвращаем имя, описание и id источника
    id: int

    class Config:
        from_attributes = True

class SourceUpdate(BaseModel): #тут будет UPDATE, обновить можно будет все
    name: Optional[str] = None
    description: Optional[str] = None