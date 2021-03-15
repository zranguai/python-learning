"""
Scrapy框架的使用
    pySpider
什么是框架：
     就是一个具有很强通用性且集成了很多功能的项目模板（可以被应用在各种需求中）
- scrapy集成好的功能：
    - 高性能的数据解析操作（xpath）
    - 高性能的数据下载：基于异步
    - 高性能的持久化存储
    - 中间件：拦截请求和响应
    - 全栈数据爬取操作
    - 分布式：redis
    - 请求传参的机制（深度爬取：每一层爬取）
    - scrapy中合理的应用selenium
环境的安装：
        a. pip3 install wheel

        b. 下载twisted http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

        c. 进入下载目录，执行 pip3 install Twisted‑17.1.0‑cp35‑cp35m‑win_amd64.whl

        d. pip3 install pywin32

        e. pip3 install scrapy
- 创建工程：cd 进入：该项目创建到哪里
    - scrapy startproject ProName
    - cd ProName
    - scrapy genspider spiderName www.xxx.com :创建爬虫文件
    - 执行：scrapy crawl spiderName
    - settings:
        - 不遵从robots协议
        - UA伪装
        - LOG_LEVEL = 'ERROR'
        - LOG_FILE = 'log.txt'

 - scrapy的数据解析
    - extract():列表是有多个列表元素
    - extract_first():列表元素只有单个

 - scrapy的持久化存储

    - 基于终端指令：
        - 只可以将parse方法的返回值存储到磁盘文件中
        - scrapy crawl first -o file.csv

    - 基于管道：pipelines.py
        - 编码流程：
            - 1.数据解析
            - 2.在item的类中定义相关的属性
            - 3.将解析的数据存储封装到item类型的对象中.item['p']
            - 4.将item对象提交给管道
            - 5.在管道类中的process_item方法负责接收item对象，然后对item进行任意形式的持久化存储
            - 6.在配置文件中开启管道
         - 细节补充：
            - 管道文件中的一个管道类表示将数据存储到某一种形式的平台中。
            - 如果管道文件中定义了多个管道类，爬虫类提交的item会给到优先级最高的管道类。
            - process_item方法的实现中的return item的操作表示将item传递给下一个即将被执行的管道类
"""