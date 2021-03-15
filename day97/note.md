+ 基于Spider父类进行全站数据的爬取
    + 全站数据的爬取：将所有页码对应的页面数据进行爬取
    + 手动请求的发送：
        + yield scrapy.Request(url, callback)
    + 对yield的总结
        + 向管道提交item的时候:yield item
        + 手动发送请求:yield scrapy.Request(url,callback)
    + 手动发起post请求：
        + yield scrapy.FormRequest(url, formdata, callback):formdata是一个字典标识的是请求参数
+ scrapy五大核心组件
    + 引擎(Scrapy)
        + 用来处理整个系统的数据流处理, 触发事务(框架核心)
    + 调度器(Scheduler)
        + 用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
    + 下载器(Downloader)
        + 用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)
    + 爬虫(Spiders)
        + 爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面
    + 项目管道(Pipeline)
        + 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
+ scrapy的请求传参
    + 作用：实现深度爬取。
    + 使用场景：如果使用scrapy爬取的数据没有存在同一张页面中
    + 传递item:yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
    + 接受item:response.meta
+ 提升scrapy爬取数据的效率
    + 在配置文件中进行相关的配置即可
        + 增加并发：
            + 默认scrapy开启的并发线程为32个，可以适当进行增加。在settings配置文件中修改CONCURRENT_REQUESTS = 100值为100,并发设置成了为100。

        + 降低日志级别：
            + 在运行scrapy时，会有大量日志信息的输出，为了减少CPU的使用率。可以设置log输出信息为INFO或者ERROR即可。在配置文件中编写：LOG_LEVEL = ‘INFO’

        + 禁止cookie：
            + 如果不是真的需要cookie，则在scrapy爬取数据时可以禁止cookie从而减少CPU的使用率，提升爬取效率。在配置文件中编写：COOKIES_ENABLED = False

        + 禁止重试：
            + 对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。在配置文件中编写：RETRY_ENABLED = False

        + 减少下载超时：
            + 如果对一个非常慢的链接进行爬取，减少下载超时可以能让卡住的链接快速被放弃，从而提升效率。在配置文件中进行编写：DOWNLOAD_TIMEOUT = 10 超时时间为10s
+ scrapy的中间件
    + 爬虫中间件
    - 下载中间件（***）：处于引擎和下载器之间
        - 作用：批量拦截所有的请求和响应
        - 为什么拦截请求
            - 篡改请求的头信息（UA伪装）
            - 修改请求对应的ip（代理）
        - 为什么拦截响应
            - 篡改响应数据，篡改响应对象
    + 爬取网易新闻的新闻标题和内容
        + 分析
            + 1.每一个板块对应的新闻数据都是动态加载出来的
    + selenium在scrapy中的使用流程
        + 在爬虫中定义一个bro的属性，就是实例化的浏览器对象
        + 在爬虫中重写父类的一个closed(self, spider),在方法中关闭bro
        + 在中间件中进行浏览器自动化的操作
        
    + 作业：
        + 网易新闻
        + 站长素材中的图片数据进行爬取