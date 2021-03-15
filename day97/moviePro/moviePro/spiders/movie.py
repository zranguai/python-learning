import scrapy
from moviePro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/index.php/vod/show/class/喜剧/id/6/page/1.html']
    url = 'http://www.4567kan.com/index.php/vod/show/class/喜剧/id/6/page/%d.html'
    # 专门用于解析电影名称
    page = 1    # 该page给之后递归调用停止用
    def parse(self, response):
        print(f'正在爬取第{self.page}页的数据')
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = MovieproItem()
            name = li.xpath('./div/a/@title').extract_first()
            item['name'] = name
            detail_url = 'http://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()
            # 可以对详情页的url手动发起请求
            # 请求参数：让Request将一个数据值(字典)传递给回调函数
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
        if self.page < 5:
            self.page += 1
            new_url = format(self.url%self.page)
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc
        yield item






















