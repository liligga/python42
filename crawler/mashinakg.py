import httpx
from parsel import Selector

# httpx - sync, async
# requests - sync
# crawler, scraper, parser

MAIN_URL = "https://www.mashina.kg/search/all/"
def get_page():
    response = httpx.get(MAIN_URL, timeout=10)
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


if __name__ == "__main__":
    page = get_page()
    # print(page[:300])
    # title = get_page_title(page)
    # print(title)
    links = get_links(page)
    print(links)