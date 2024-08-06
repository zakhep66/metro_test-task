from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.news import NewsEntity


class NewsORM:
	__tablename__ = "news"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	content: Mapped[str]
	date: Mapped[str]

	def to_entity(self) -> NewsEntity:
		return NewsEntity(
			id=self.id,
			title=self.title,
			image_url=self.content,
			date=self.date,
		)

	@staticmethod
	def from_entity(obj: NewsEntity) -> "NewsORM":
		return NewsORM(
			id=obj.id,
			title=obj.title,
			content=obj.image_url,
			date=obj.date,
		)
