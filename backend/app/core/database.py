from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.database_url) #создание движка 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # фабрика сессий

Base = declarative_base() #базовый класс моделей

#функция-генератор, нужна чтобы FastAPI мог открывать сессию к базе и закрывать после отправки ответа
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#тут настраивается движок подключения