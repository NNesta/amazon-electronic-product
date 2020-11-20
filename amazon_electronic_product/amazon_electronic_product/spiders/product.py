import scrapy
from ..items import ProductItem


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/b?node=16225009011&pf_rd_r=T8NBA5MTDVB4CWBYN5QF&pf_rd_p=5232c45b-5929-4ff0-'
        '8eae-5f67afd5c3dc'
    ]

    def parse(self, response):
        items = ProductItem()
        items['Name'] = response.xpath("//a[@class='a-link-normal s-access-detail-page s-color-twister-title-link "
                                       "a-text-normal']/@title").getall()
        items['Price'] = response.xpath("//a/span[@class='a-size-base a-color-base']/text()"
                                        " | //div/div/div/div[@class='a-row a-spacing-none']/span[@class='a-size-small"
                                        " a-color-secondary']/text()").getall()
        items['Manufacturer'] = response.xpath("//span[@class='a-size-small a-color-secondary/text()'][2]").getall()
        items['Ratings'] = response.xpath("//span/span/a/i/span[@class='a-icon-alt']/text()").getall()
        items['Reviews'] = response.xpath("//li/div/div/a[@class='a-size-small a-link-normal a-text-normal']"
                                          "/text()").getall()
        items['image_link'] = response.xpath("//div[@class='a-row a-spacing-base']/div/div/descendant::node()/img/@src")
        yield items

