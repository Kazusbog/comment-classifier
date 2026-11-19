from sqlalchemy.orm import Session
from app.models.source import Source
from app.schemas.source import SourceCreate
from app.schemas.source import SourceCreate, SourceUpdate

def get_sources(db: Session, skip: int = 0, limit: int = 100): #получает список источников из БД для отображения на фронтенде
    return db.query(Source).offset(skip).limit(limit).all()

def create_source(db: Session, source: SourceCreate): #создает новый источник в БД на основе данных, переданных в объекте SourceCreate.
    db_source = Source(name=source.name, description=source.description)
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source

def get_source(db: Session, source_id: int): #получает источник из БД по его id
    return db.query(Source).filter(Source.id == source_id).first()

def update_source(db: Session, source_id: int, source_update: SourceUpdate):
    db_source = get_source(db, source_id)
    if not db_source:
        return None
    
    update_data = source_update.model_dump(exclude_unset=True) #достает только те поля, которые были переданы в запросе на обновление
    for key, value in update_data.items():
        setattr(db_source, key, value)

    db.commit()
    db.refresh(db_source)
    return db_source

def delete_source(db: Session, source_id: int):
    db_source = get_source(db, source_id)
    if not db_source:
        return None
    
    db.delete(db_source)
    db.commit()
    return db_source

