from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import select

from app.gateways.postgres.database import Database
from app.gateways.postgres.models.news import NewsORM


class INewsRepository(ABC):
	@abstractmethod
	async def get_news_by_period(self, from_date: str, to_date: str) -> list[NewsORM]:
		...

	@abstractmethod
	async def create_news(self, new: NewsORM) -> NewsORM:
		...


@dataclass
class ORMUserRepository(INewsRepository):
	database: Database

	async def get_news_by_period(self, from_date: str, to_date: str) -> list[NewsORM]:
		stmt = select(NewsORM).where(NewsORM.date.between(from_date, to_date))
		async with self.database.get_read_only_session() as session:
			return await session.scalars(stmt)

	async def create_news(self, news: NewsORM) -> NewsORM:
		async with self.database.get_session() as session:
			session.add(news)
		return news
