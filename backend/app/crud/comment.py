from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate
from app.schemas.comment import CommentCreate, CommentUpdate

def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Comment).offset(skip).limit(limit).all()

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def create_comment(db: Session, comment: CommentCreate, sentiment: str = None):
    db_comment = Comment(
        text=comment.text,
        sentiment=sentiment,
        source_id=comment.source_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, comment_update: CommentUpdate): #comment_update - содержит данные для обновления комментария
    db_comment = get_comment(db, comment_id) #достает комментарий из базы данных по его id
    if not db_comment:
        return None
    
    update_data = comment_update.model_dump(exclude_unset=True) #достает только те поля, которые были переданы в запросе на обновление
    for key, value in update_data.items():
        setattr(db_comment, key, value)

    db.commit() #сохраняет изменения в базе данных
    db.refresh(db_comment) #обновляет объект комментария в памяти, чтобы он содержал актуальные данные из базы данных
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = get_comment(db, comment_id)
    if not db_comment:
        return None
    db.delete(db_comment)
    db.commit()
    return db_comment