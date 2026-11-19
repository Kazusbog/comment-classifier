from pydantic import BaseModel, Field
from typing import Optional

class CommentBase(BaseModel): #тут описана схема валидации данных для модели Comment
    text: str = Field(..., min_length=1, description="Текст комментария не может быть пустым")
    source_id: Optional[int] = None

class CommentCreate(CommentBase): #при создании комментария, мы можем передать только текст и id источника
    pass

class CommentResponse(CommentBase): #при ответе на запрос, мы возвращаем текст, id источника, id комментария и его сентимент
    id: int
    sentiment: Optional[str] = None

    class Config:
        from_attributes = True

class CommentUpdate(BaseModel): #тут будет UPDATE, обновить можно будет все
    text: Optional[str] = None
    sentiment: Optional[str] = None
    source_id: Optional[int] = None
