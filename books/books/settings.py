import os

# Project name
BOT_NAME = "books"

# Modules where spiders are defined
SPIDER_MODULES = ["books.spiders"]
NEWSPIDER_MODULE = "books.spiders"

# Respect robots.txt rules
ROBOTSTXT_OBEY = True

# MongoDB connection settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # Default for local use
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "books_db")

# Configure item pipelines and their priority
ITEM_PIPELINES = {
    "books.pipelines.MongoPipeline": 300,
}

# Use modern Twisted reactor for asyncio compatibility
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Ensure UTF-8 encoding for exported data
FEED_EXPORT_ENCODING = "utf-8"
