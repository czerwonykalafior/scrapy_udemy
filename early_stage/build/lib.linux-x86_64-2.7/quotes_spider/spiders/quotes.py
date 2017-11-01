from scrapy import Spider
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem



class Udemy_1_Spider(Spider):
    name = 'udemy_1_quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)
        yield l.load_item()
        #
        # quotes = response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     text = quote.xpath('.//*[@class="text"]/text()').extract()
        #     author = quote.xpath('.//*[@itemprop="author"]/text()').extract()
        #     tags = quote.xpath('.//*[@itemprop="author"]/text()').extract()
        #
        #
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        #
        # yield Spider.Request(absolute_next_page_url)


