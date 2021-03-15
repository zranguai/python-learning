# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep


class WangyiproDownloaderMiddleware:



    #参数：
    #reuqest:拦截到请求对应的响应对象
    #response：拦截到所有的响应对象（1+5+n）
    #spider：爬虫类实例化的对象，可以实现爬虫类和中间件类的数据交互
    def process_response(self, request, response, spider):
        #拦截到5个板块对应的响应对象，将其替换成5个符合需求的新的响应对象进行返回
        #1.找出5个板块对应的5个不符合需求的响应对象
        if request.url in spider.model_urls:
            #就是满足需求的五个板块对应的响应对象
            #url:响应对象对应的请求对象的url
            #body:响应数据,可以由selenium中的page_source返回
            bro = spider.bro
            bro.get(request.url)
            sleep(3)
            page_text = bro.page_source    # 包含了动态加载的新闻数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            return response


