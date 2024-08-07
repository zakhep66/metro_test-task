from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.models import News as NewsModel
from .schemas import News as NewsSchema


async def get_news_by_period(session: AsyncSession, days: int) -> list:
    cutoff_date = datetime.now() - timedelta(days=days)
    stmt = select(NewsModel).filter(NewsModel.date.between(cutoff_date, datetime.now()))
    result = await session.execute(stmt)
    news = result.scalars().all()
    return list(news)


async def add_news(session: AsyncSession, news: NewsSchema) -> NewsModel:
    new = NewsModel(**news.model_dump())
    session.add(new)
    await session.commit()
    return new


async def is_distinct_news(session: AsyncSession, news: NewsSchema) -> bool:
    stmt = select(NewsModel).filter_by(title=news.title, date=news.date)
    result = await session.execute(stmt)
    existing_news = result.scalars().first()
    return existing_news is None
