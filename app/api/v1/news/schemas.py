from datetime import datetime

from pydantic import BaseModel, ConfigDict


class News(BaseModel):
	model_config = ConfigDict(
		from_attributes=True,
	)
	title: str
	img_url: str
	date: datetime

