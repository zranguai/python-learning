import scrapy
from homeworkPro.items import HomeworkproItem

class HomeworkSpider(scrapy.Spider):
    name = 'homework'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huya.com/g/huwai']
    # 基于管道存储
    def parse(self, response):
        li_list = response.xpath('//*[@id="js-live-list"]/li')
        for li in li_list:
            title = li.xpath('./a[2]/text()').extract_first()
            author = li.xpath('./span/span[1]/i/text()').extract_first()
            hot = li.xpath('./span/span[2]/i[2]/text()').extract_first()
            # 定义相关属性
            item = HomeworkproItem()
            # 将解析的数据存储封装到item类型的对象中.item['p']
            item['title'] = title
            item['author'] = author
            item['hot'] = hot
            # 将item对象提交给管道
            yield item
