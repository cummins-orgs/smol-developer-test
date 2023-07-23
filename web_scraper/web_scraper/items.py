```python
import scrapy

class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    post_date = scrapy.Field()
```