# https://www.cnblogs.com/bobo-zhang/p/11243138.html

# 中国空气质量在线检测    反爬虫有点强
# https://www.aqistudy.cn/html/city_detail.html
# 针对网页不能右键打开：https://blog.csdn.net/Sily_Z/article/details/81776284


# 测试：
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Cookie': 'UM_distinctid=175bf66cd71242-0fe0c5ed2f7aeb-3d634d00-144000-175bf66cd727b6; CNZZDATA1254317176=1408543989-1605614792-%7C1605701843; CNZZDATA5808503=cnzz_eid%3D1695823772-1605230250-%26ntime%3D1605704672'
}
url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8D%97%E6%98%8C'
response = requests.get(url=url, headers=headers).text
print(response)