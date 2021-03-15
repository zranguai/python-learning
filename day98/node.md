+ 图片懒加载
    + 应用到标签的伪属性，数据捕获的时候一定是基于伪属性进行！！！
+ ImagePileline: 专门用作与二进制数据下载和持久化存储的管道类

+ CrawlSpider
    + 一种基于scrapy进行全站数据爬取的一种新的技术手段
    + CrawlSpider就是Spider的一个子类
        + 连接提取器：LinkExtractor
        + 规则解析器：Rule
    + 使用流程
        + 新建一个工程
        + cd 工程中
        + 新建一个爬虫文件 scrapy genspider -t crawl spiderName www.xxx.com

+ 分布式
    + 概念：需要搭建一个分布式的集群，然后在机群的每一台电脑中执行同一组程序，让其对某一个网站的数据进行联合分布爬取
    + 原生的scrapy框架是不可以实现分布式？
        + 因为调度器不可以被共享
        + 管道不可以被共享
    + 如何实现分布式？
        + scrapy+scrapy-redis实现分布式
    + scrapy-redis组件的作用是什么？
        + 可以提供可被共享的调度器和管道
        + 特性：数据只可以存储到redis数据库
    + 分布式的实现流程:
        + 1.pip install scrapy-redis
        + 2.创建工程
        + 3.cd 工程目录中
        + 4.创建爬虫文件(a.创建基于Spider的爬虫文件b.创建CrawlSpider的爬虫文件)
        + 5.修改爬虫类
            + 导报：from scrapy-redis.spiders import RedisCrawlSpider
            + 修改当前爬虫类的父类为RedisCrawlSpider
            + allowed_domains和start_urls删除
            + 添加一个新属性:redis_key = 'fbsQueue',表示的是可以被共享的调度器队列的名称
            + 编写爬虫类的其他操作(常规操作)
        + 6.settings配置文件的配置
            - UA伪装
            - Robots
            - 管道的指定
                    ITEM_PIPELINES = {
                        'scrapy_redis.pipelines.RedisPipeline': 400
                    }
            - 指定调度器：
                 # 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
                DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
                # 使用scrapy-redis组件自己的调度器
                SCHEDULER = "scrapy_redis.scheduler.Scheduler"
                # 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
                SCHEDULER_PERSIST = True
            - 指定redis数据库
                REDIS_HOST = 'redis服务的ip地址'
                REDIS_PORT = 6379

            - redis的配置文件进行配置redis.windows.conf：
                - 关闭默认绑定：56Line：#bind 127.0.0.1
                - 关闭保护模式：75Line：protected-mode no
            - 启动redis的服务端和客户端：
                - redis-server.exe redis.windows.conf
                - redis-cli

            - 启动程序：
                scrapy runspider xxx.py
            - 向调度器的队列中仍入一个起始的url：
                - 队列是存在于redis中
                - 开启redis的客户端： lpush fbsQueue http://wz.sun0769.com/index.php/question/questionType?type=4&page=

- 增量式
    - 概念：用于监测网站数据更新的情况。
    - 核心机制：去重。redis的set实现去重

+ 总结反爬机制：
    + robots
    + UA伪装
    + 验证码
    + 代理
    + cookie
    + 动态变化的请求参数
    + js加密
    + js混淆
    + 图片懒加载
    + 动态数据的捕获
    + seleium:规避检测
