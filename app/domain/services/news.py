from abc import ABC, abstractmethod

from app.domain.entities.news import NewsEntity


class INewsService(ABC):
	@abstractmethod
	async def get_news_by_period(self, from_date: str, to_date: str) -> list[NewsEntity]:
		...

	@abstractmethod
	async def create_news(self, new: NewsEntity) -> NewsEntity:
		...
