from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import News
from app.core.models.db_helper import db_helper
from .services import get_news_by_period


router = APIRouter(tags=['news'])


@router.get('/news/{days}', response_model=list[News])
async def get_news_by_period_handler(
		days: int = Path(gt=0, lt=100_000),
		session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list:
	return await get_news_by_period(session=session, days=days)
