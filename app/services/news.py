from dataclasses import dataclass

from app.domain.entities.news import NewsEntity
from app.domain.services.news import INewsService
from app.gateways.postgres.models.news import NewsORM
from app.gateways.postgres.repositories.news import INewsRepository


@dataclass
class ORMNewsService(INewsService):
	repository: INewsRepository

	async def get_news_by_period(self, from_date: str, to_date: str) -> list[NewsEntity]:
		news_dto = await self.repository.get_news_by_period(from_date, to_date)
		return [news.to_entity() for news in news_dto]

	async def create_news(self, new: NewsEntity) -> NewsEntity:
		new_dto = await self.repository.create_news(NewsORM.from_entity(new))
		return new_dto.to_entity()
