import asyncio
import httpx
from parsel import Selector
from time import perf_counter

# httpx - sync, async
# requests - sync
# crawler, scraper, parser

MAIN_URL = "https://www.mashina.kg/search/all/"
async def get_page(client, page_number: int = 1):
    response = await client.get(
        f"{MAIN_URL}?region=all&page={page_number}", timeout=10
    )
    print(f"Пришел ответ на запрос страницы {page_number}")
    # print("Status code", response.status_code)
    return response.text

def get_page_title(page):
    selector = Selector(text=page)
    title = selector.css("title::text").get()
    return title

def get_links(page):
    selector = Selector(text=page)
    links = selector.css("div.list-item a::attr(href)").getall()
    return list(map(lambda x: "https://www.mashina.kg" + x, links))

async def get_all_links():
    tasks = []
    async with httpx.AsyncClient() as client:
        for i in range(1, 5):
            task = asyncio.create_task(get_page(client=client, page_number=i))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for page in results:
            pass

    

if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(get_all_links())
    end = perf_counter()
    print(f"It took {end-start} sec")