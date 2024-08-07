from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.news.schemas import News
from app.api.v1.news.services import add_news


async def fetch_news(session):
    url = "http://mosday.ru/news/tags.php?metro"
    async with session.get(url) as response:
        return await response.text()


async def parse_news(session: AsyncSession):
    async with aiohttp.ClientSession() as http_session:
        html = await fetch_news(http_session)
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', attrs={"width": "95%", "cellspacing": "10"})

        # Перебираем все строки таблицы
        for row in table.find_all('tr'):
            title_element = row.find('font', attrs={"size": "3", "style": "font-size:16px"})
            image_element = row.find('img')
            date_element = row.find('b', string=lambda text: isinstance(text, str) and len(text) == 10)

            # Проверяем, что элементы найдены, прежде чем извлекать текст
            if title_element and image_element and date_element:
                title = title_element.text
                image_url = image_element['src']
                published_date = date_element.text

                news_data = News(title=title, img_url=image_url, date=datetime.strptime(published_date, '%d.%m.%Y'))
                await add_news(session, news_data)
