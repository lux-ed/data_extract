import scrapy

class BlogSpider(scrapy.Spider):

    name = 'spider'
    start_urls = ['https://www.imdb.com/list/ls055592025/']

    def parse(self, response):
        for title in response.css('.lister-item-header>a'):
            yield {'title': title.css('a ::text').extract_first()}
