from fastapi import APIRouter

from .news.handlers import router as news_router


router = APIRouter()

router.include_router(news_router, prefix='/news', tags=['news'])
