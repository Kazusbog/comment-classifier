from fastapi import APIRouter, Depends, HTTPException, status #базовые библиотеки для работы с маршрутизацией, зависимостями и статусами HTTP-ответов
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List


from app.core.database import get_db #функция get_db открывает сессию к базе данных и закрывает её после отправки ответа
from app.schemas.source import SourceResponse, SourceCreate, SourceUpdate #функции CRUD
from app.crud import source as crud_source #импортируем модуль crud_source, который содержит функции для работы с источниками в базе данных

router = APIRouter(prefix="/sources", tags=["sources"])

@router.post("/", response_model=SourceResponse, status_code=status.HTTP_201_CREATED)
def create_new_source(source: SourceCreate, db: Session = Depends(get_db)):
    try:
        return crud_source.create_source(db=db, source=source)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Источник с таким названием уже существует"
        )

@router.get("/", response_model=List[SourceResponse])
def read_sources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_source.get_sources(db=db, skip=skip, limit=limit) #получает список источников из базы данных для отображения на фронтенде

@router.get("/{source_id}", response_model=SourceResponse)
def read_source(source_id: int, db: Session = Depends(get_db)):
    db_source = crud_source.get_source(db=db, source_id=source_id)
    if db_source is None:
        raise HTTPException(status_code=404, detail="Источник не найден")
    return db_source

@router.patch("/{source_id}", response_model=SourceResponse)
def update_source(source_id: int, source: SourceUpdate, db: Session = Depends(get_db)):
    db_source = crud_source.update_source(db=db, source_id=source_id, source_update=source)
    if db_source is None:
        raise HTTPException(status_code=404, detail="Источник не найден")
    return db_source

@router.delete("/{source_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_source(source_id: int, db: Session = Depends(get_db)):
    db_source = crud_source.delete_source(db=db, source_id=source_id)
    if db_source is None:
        raise HTTPException(status_code=404, detail="Источник не найден")
    return None