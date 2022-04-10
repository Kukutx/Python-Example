import asyncio
import time

async def request(url):
    print('正在请求url：',url)
    # time.sleep(2)            #在异步协程中如果出现了同步模块的相关代码，那么就无法实现异步
    await asyncio.sleep(2)     #异步模块相关代码，当asyncio中遇到阻塞操作必须进行手动挂起 await
    print('请求成功：',url)
start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.google.com'
]
#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c= request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time() - start)

