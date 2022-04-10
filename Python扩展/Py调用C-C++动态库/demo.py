import time
from ctypes import *
myso = CDLL("./demo.dll")
ts = time.time()
c = myso.my_app(100000000)
print("time spend ",time.time()-ts,c)
def my_add(a):
    ret = 0
    for i in range(a):
        ret += 2
    return(ret)
ts = time.time()
d = my_add(100000000)
print("time spend ",time.time()-ts,d)


mydll = CDLL("./PyDLL.dll")
a=mydll.add(1,3)
print(a)

# 使用64-bit的python 无法调用 32-bit的*.dll,如果想使用64位dll可以使用vs设置64位编译