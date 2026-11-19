from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.comment import CommentCreate, CommentResponse, CommentUpdate
from app.crud import comment as crud_comment
from app.crud import source as crud_source

#создается мини приложение (роутер) и автоматически добавляем /comments ко всем путям внутри файла
router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED) #принимает POST-запрос
def create_new_comment(comment: CommentCreate, db: Session = Depends(get_db)): #db: Session - механизм внедрения зависимостей в FastAPI

    if comment.source_id is not None:
        if not crud_source.get_source(db=db, source_id=comment.source_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Источник с id={comment.source_id} не найден"
            )
    # тут будет бизнес логика
    predicted_sentiment = "positive" if "хорош" in comment.text.lower() else "neutral"

    return crud_comment.create_comment(db=db, comment=comment, sentiment=predicted_sentiment)


@router.get("/", response_model=List[CommentResponse]) # принимает GET-запрос и достает список комментов из БД
def read_comments(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return crud_comment.get_comments(db=db, skip=skip, limit=limit)

@router.get("/{comment_id}", response_model=CommentResponse) #GET запрос с конкретным ID
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_comment.get_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.patch("/{comment_id}", response_model=CommentResponse) #PATCH запрос с конкретным ID
def update_comment(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)):
    if comment.source_id is not None:
        if not crud_source.get_source(db=db, source_id=comment.source_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Источник с id={comment.source_id} не найден"
            )
    db_comment = crud_comment.update_comment(db=db, comment_id=comment_id, comment_update=comment)
    return db_comment

@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT) #DELETE запрос с конкретным ID
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_comment.delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return None