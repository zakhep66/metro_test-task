from datetime import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class News(Base):
	title: Mapped[str]
	img_url: Mapped[str]
	date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
