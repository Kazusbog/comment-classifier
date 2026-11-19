from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.comments import router as comments_router
from app.api.sources import router as sources_router

app = FastAPI(
    title="Comment Classifier API",
    version="1.0.0"
)

# разрешаем запросы с фронта на будущее
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comments_router) #подключили маршруты для работы с комментариями
app.include_router(sources_router) #подключили маршруты для работы с источниками

@app.get("/")
def root():
    return {"message": "Comment Classifier API is running"}