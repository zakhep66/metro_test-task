from sqlalchemy.orm import Mapped

from .base import Base


class News(Base):
	title: Mapped[str]
	img_url: Mapped[str]
	date: Mapped[str]
