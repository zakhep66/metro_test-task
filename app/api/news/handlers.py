import datetime

from fastapi import APIRouter


router = APIRouter(tags=["News"])


@router.get(
	'/',
	description="Получить новости за указанные период",
)
async def get_news(from_date: str, to_date: str = datetime.datetime.now()):
	"""Получить новости за указанные период"""
	...
