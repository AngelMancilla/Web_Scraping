# Books Scraper 📚

This is a web scraping project built with [Scrapy](https://scrapy.org/) that extracts book information from [Books to Scrape](http://books.toscrape.com), a site designed for web scraping practice. The scraped data, including book titles, prices, and URLs, is stored in a MongoDB database for later analysis or use.

---

## Features
- Scrapes book details such as:
  - **URL**: The book's page link.
  - **Title**: The title of the book.
  - **Price**: The book's price.
- Handles **pagination** to scrape all available books across multiple pages.
- Stores the scraped data in **MongoDB** using a custom pipeline.
- **Environment-variable-based configuration** for flexibility and security.

---

By AngelMancilla 
