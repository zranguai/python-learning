# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 专门用作于持久化存储
class FirstbloodPipeline:
    fp = None
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('./data.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        content = item['content']
        self.fp.write(content)
        return item
    def close_spider(self, spider):
        print('我只会在爬虫结束的时候调用一次')
        self.fp.close()
