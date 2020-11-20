# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):

    Name = scrapy.Field()
    Price = scrapy.Field()
    Manufacturer = scrapy.Field()
    Ratings = scrapy.Field()
    Reviews = scrapy.Field()
    image_link = scrapy.Field()

