import scrapy
from ..items import ProductItem


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        items = ProductItem()
        items['name'] = response.xpath().get()
        items['price'] = response.xpath().get()
        yield items

