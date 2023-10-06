```python
import scrapy
from scrapy.loader import ItemLoader
from web_scraper.web_scraper.items import CraigslistItem

class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://www.craigslist.org/"]

    def parse(self, response):
        for post in response.css('.result-row'):
            loader = ItemLoader(item=CraigslistItem(), selector=post)
            loader.add_css('title', '.result-title::text')
            loader.add_css('link', 'a::attr(href)')
            loader.add_css('date', '.result-date::attr(datetime)')
            loader.add_css('price', '.result-price::text')
            yield loader.load_item()

        next_page = response.css('a.button.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```