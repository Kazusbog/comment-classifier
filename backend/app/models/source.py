from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Source(Base): #тут описана модель Source, которая представляет источник данных в базе данных
    __tablename__ = "sources" #имя таблицы

    id = Column(Integer, primary_key=True, index=True)#эта строчка и 2 дальше - поля таблицы, которые будут храниться в базе данных
    name = Column(String, unique=True, nullable=False)
    description=Column(String, nullable=True)

    #Обратная связь, можно будет получить список всех комментов этого сорса
    comments = relationship("Comment", back_populates="source")

