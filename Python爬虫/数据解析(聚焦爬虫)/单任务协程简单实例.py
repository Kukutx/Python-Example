import asyncio

# # 单线程（单任务）协程实例
# async def request(url):                    #定义一个协程
#     print('正在请求url：',url)
#     print('请求成功：',url)
# #async修饰的函数，返回协程对象
# c = request('www.baidu.com')

# #event_loop
# #创建一个事件循环对象
# loop = asyncio.get_event_loop()   #event_loop事件对象，相当于一个无限循环，可以把函数注册到这个事件循环上，当满足某些条件的时候，函数就会循环执行
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# #task （任务，它是对协程对象的进一步封装，包含了任务的各种状态）
# loop = asyncio.get_event_loop()
# #基于loop创建一个task任务对象
# task = loop.create_task(c)            
# print(task)             #会显示执行时
# loop.run_until_complete(task)
# print(task)             #会显示执行后

#future    (实际上跟task没啥区别) 代表执行或未执行的任务
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)        
# print(task)    


async def request(url):                  
    print('正在请求url：',url)
    print('请求成功：',url)
    return url
c = request('www.baidu.com')
def callback_func(task):
    print(task.result())          #result返回的就是任务对象中封装的协程对象对应的函数返回值
#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
