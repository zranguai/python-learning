import scrapy
from wangyiPro.items import WangyiproItem
from selenium import webdriver
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls = []
    bro = webdriver.Chrome(executable_path=r'D:\老男孩python22期代码及笔记\day95\chromedriver.exe')
    def parse(self, response):
        # 解析出5个板块对应的url
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        model_index = [3,4,6,7,8]
        for index in model_index:
            li = li_list[index]
            # 5个板块对应的url
            model_url = li.xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
            # 对每一个板块的url进行手动请求的发送
            yield scrapy.Request(model_url, callback=self.parse_model)
    def parse_model(self, response):    # 用作于解析每一个板块对应页面数据中的新闻标题和新闻详情页的url
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item = WangyiproItem()
            item['title'] = title
            detail_url = div.xpath('./a/@herf').extract_first()
            yield scrapy.Request(detail_url, callback=self.parse_new_detail, meta={'item': item})
    def parse_new_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item['content'] = content
        yield item
    # 改方法只会在整个程序结束时执行一次
    def closed(self, reason):
        self.bro.quit()

