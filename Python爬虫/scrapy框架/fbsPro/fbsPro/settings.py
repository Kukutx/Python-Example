# Scrapy settings for fbsPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fbsPro'

SPIDER_MODULES = ['fbsPro.spiders']
NEWSPIDER_MODULE = 'fbsPro.spiders'

LOG_LEVEL = "ERROR"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'fbsPro.middlewares.FbsproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'fbsPro.middlewares.FbsproDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'fbsPro.pipelines.FbsproPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 
# 指定scrapy_redis组件封装好的共享管道
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 400,
}
# 指定scrapy_redis组件调度器
# 添加一个去重容器类的配置，作用使用Redis的set集合来存储请求的指纹数据，从而实现请求去重持久化
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis组件调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器是否要持久化，也就是当爬虫结束了，是否清空Redis中的请求队列和去重指纹的set,其实就是爬虫进度如果某台机群突然宕机了重新启动的话会重新在之前的进度继续如果是False那就是从0开始
SCHEDULER_PERSIST = True

# 指定redis服务器
REDIS_HOST = '127.0.0.1'                   #redis服务器地址（建议远程服务器ip）
REDIS_PORT = 6379





# redis相关操作以及配置redis配置文件：
# 1.将redis.windows.conf里的bind 127.0.0.1给注释掉
# 2.将redis.windows.conf里的protected-mode yes 改成no  （关闭保护模式）
# 3.启动redis数据库 redis-server
# 4.启动redis客户端 redis-cli
# 5.执行工程 scrapy runspider fbs.py
# 6.向调度器的队列中放入一个起始url：调度器的队列在redis的客户端中 lpush sun https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1 (将调度器丢入起始url就能进行数据的爬取了)
    #使用过的redis数据库命令   
    # keys *   #查看本地数据存储
    # lrange fbs:items 0 -1  #从0查到尾
    # llen fbs:items  查看爬取了多少数据
# 7.指定redis服务器（用于指定redis服务器如果不指定只会存储到本机redis）







