import scrapy

class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://ip.chinaz.com/']

    def parse(self, response):
        page_text = response.text
        with open('iip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
