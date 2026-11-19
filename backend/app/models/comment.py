from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Comment(Base): #тут описана модель Comment, которая представляет комментарии в базе данных
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True) #эта строчка и 2 дальше - поля таблицы, которые будут храниться в базе данных
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=True)

    #FK на sources
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)

    #связь с sources
    source = relationship("Source", back_populates="comments")