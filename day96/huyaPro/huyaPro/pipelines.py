# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HuyaproPipeline:
    fp = None
    def open_spider(self, spider):
        print('open')
        self.fp = open('huyazhibo.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):    # item就是接受爬虫类提交过来的item对象
        self.fp.write(item['title']+':'+item['author']+':'+item['hot']+'\n')
        print(item['title']+'写入成功')
        return item    # item的操作表示将item传递给下一个即将被执行的管道类
    def close_item(self, spider):
        self.fp.close()
        print('close')

class mysqlPopeLine:
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='Spider', charset='utf8')
        print(self.conn)
    def process_item(self, item, spider):
        sql = 'insert into huya values("%s","%s","%s")'%(item['title'],item['author'],item['hot'])
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


