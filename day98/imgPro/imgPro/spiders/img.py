import scrapy
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/meinvtupian.html']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            img_src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            item = ImgproItem()
            item['img_src'] = img_src
            yield item
            # print(img_src)
