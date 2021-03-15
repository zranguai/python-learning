# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
]
from itemadapter import is_item, ItemAdapter
class MiddleproDownloaderMiddleware:
    # 拦截正常请求
    def process_request(self, request, spider):
        # 进行UA伪装
        print('!!!!!!!!!!!!!!!!!!!!!')
        request.headers['User-Agent'] = random.choice(user_agent_list)
        print(request.headers['User-Agent'])
        # 代理ip
        request.meta['proxy'] = 'http://123.55.114.25:9999'
        print(request.meta['proxy'])
        return None
    # 拦截所有的请求
    def process_response(self, request, response, spider):
        print('??????????????????')
        return response
    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        # print(request)
        return request    # 将修正后的正常的请求对象进行重新发送

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
