# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
# 存储到mysql数据库中
class HomeworkproPipeline:
    conn = None
    cursor = None
    def open_spider(self, spider):
        # 1.连接数据库
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='homeworkPro', charset='utf8')
    def process_item(self, item, spider):
        sql = 'insert into hwk values("%s","%s","%s")' % (item['title'], item['author'], item['hot'])
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