from itemadapter import ItemAdapter
import pymysql

class WangyiproPipeline:
    conn = None
    cur = None
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='Spider', charset='utf8')
    def process_item(self, item, spider):
        print(item)
        sql = 'insert into wangyi values("%s","%s")'%(item['title'], item['content'])
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()