# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ImgproPipeline:
#     def process_item(self, item, spider):
#         return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline
class ImgproPipeline(ImagesPipeline):
    # 是用来对媒体资源进行请求的(数据下载)，参数item就是接受到爬虫类提交的item对象
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_src'])
    # 指明数据存储的路径,需要再settings.py中进行设置
    def file_path(self, request, response=None, info=None):
        return request.url.split('/')[-1]
    def item_completed(self, results, item, info):
        return item