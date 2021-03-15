import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunCrawlPro.items import SuncrawlproItem, Detail_item

class SuncrawlSpider(CrawlSpider):
    name = 'sunCrawl'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']
    # 实例化一个连接提取器对象:只能取连接
    # 作用：根据指定规则(allow='正则表达式')进行指定连接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')    # 获取页码连接
    # 获取详情页连接,注意：如果中间有点要注意转义
    link_detail = LinkExtractor(allow=r'/political/politics/index?id=\d+')
    rules = (
        # 将Link作用到了Rule构造方法的参数1中
        # 作用:(可以数据解析和请求发送)将连接提取器提取到的连接进行请求发送且根据指定规则对请求到的数据进行数据解析
        Rule(link, callback='parse_item', follow=False),
        # follow=True:将连接提取器 继续作用到 连接提取器取到的 连接 所对应的 页面中
        Rule(link_detail, callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        # xpath表达式中是不可以出现tbody的*****
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./li/span[3]/a/text()').extract_first()
            num = li.xpath('./li/span[1]/text()').extract_first()
            item = SuncrawlproItem()
            item['title'] = title
            item['num'] = num
            yield item
    def parse_detail(self, response):
        num = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        num = num.split(':')[-1]
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item = Detail_item()
        item['num'] = num
        item['content'] = content
        yield item


