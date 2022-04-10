import asyncio
import requests
import aiohttp
import time
#与flask服务器配套
start = time.time()
urls=[
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]
async def get_page(url):
    # 基于同步的网络请求模块
    # print('正在下载',url)
    # # response = requests.get(url=url)             #requests.get发出的请求是基于同步的网络请求模块
    # print('下载完毕',response.text)

    #aiohttp:基于异步网络请求模块
    async with aiohttp.ClientSession() as session:
       async with await session.get(url) as response:     #发出请求可添加参数
           page_text = await response.text()           #对获取响应数据操作之前一定要手动挂起await
           print(page_text)


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('总耗时：',end - start)