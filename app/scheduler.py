from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.models.db_helper import db_helper
from app.parser import parse_news

scheduler = AsyncIOScheduler()


async def scheduled_parse_news():
    async for session in db_helper.scoped_session_dependency():
        await parse_news(session)


def start_scheduler():
    scheduler.add_job(scheduled_parse_news, 'interval', minutes=10)
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown(wait=True)
