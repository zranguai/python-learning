import scrapy
from huyaAll.items import HuyaallItem

class HuyaSpider(scrapy.Spider):
    name = 'huya'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huya.com/g/wzry']
    url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2336&tagAll=0&page=%d'

    def parse(self, response):
        li_list = response.xpath('//*[@id="js-live-list"]/li')
        for li in li_list:
            title = li.xpath('./a[2]/text()').extract_first()
            author = li.xpath('./span/span[1]/i/text()').extract_first()
            hot = li.xpath('./span/span[2]/i[2]/text()').extract_first()
            # 定义相关属性
            item = HuyaallItem()
            # 将解析的数据存储封装到item类型的对象中.item['p']
            item['title'] = title
            item['author'] = author
            item['hot'] = hot
            # 将item对象提交给管道
            yield item
        # 手动请求的发送
        for page in range(2, 5):
            new_url = format(self.url%page)
            # 发起的是get请求
            yield scrapy.Request(url=new_url, callback=self.parse_other)
    # 所有的解析方法都必须模拟parse进行定义：必须要有和parse同样的参数
    def parse_other(self, response):
        print(response.text)



