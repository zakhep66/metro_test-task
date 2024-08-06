from dataclasses import dataclass


@dataclass(frozen=True)
class NewsEntity:
	id: int
	title: str
	image_url: str
	date: str
