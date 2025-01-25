import scrapy

class BooksItem(scrapy.Item):
    # Unique ID for the book
    _id = scrapy.Field()
    # URL of the book page
    url = scrapy.Field()
    # Title of the book
    title = scrapy.Field()
    # Price of the book
    price = scrapy.Field()

