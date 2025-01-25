import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    # Name of the spider
    name = "book"
    # Domains allowed for crawling
    allowed_domains = ["books.toscrape.com"]
    # Starting URL
    start_urls = ["https://books.toscrape.com/"]

    def start_requests(self):
        # Initialize requests for the start URLs
        for url in self.start_urls:
            yield scrapy.Request(
                url, callback=self.parse, errback=self.log_error
            )

    def parse(self, response):
        """
        Extracts book details and handles pagination.

        @url https://books.toscrape.com
        @returns items 20 20
        @returns request 1 50
        @scrapes url title price
        """
        # Loop through each book on the page
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = book.css("h3 > a::attr(href)").get()
            item["title"] = book.css("h3 > a::text").get()
            item["price"] = book.css("p.price_color::text").get()
            yield item

        # Handle pagination
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(
                url=next_page_url, callback=self.parse, errback=self.log_error
            )

    def log_error(self, failure):
        # Log errors during the request
        self.logger.error(repr(failure))
