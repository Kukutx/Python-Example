# -*- coding: utf8 -*-
# Python调用C和C++可执行程序
import subprocess      #linux上是commands
import os  
main = "testmain.exe"  
if os.path.exists(main):  
    rc, out = subprocess.getstatusoutput(main) 
    print ('rc = %d, \nout = %s' % (rc, out))  
print ('*'*10)  
f = os.popen(main)    
data = f.readlines()    
f.close()    
print (data)  
print ('*'*10)  
os.system(main)

# 运行方法（只有这种不是生成.so然后让python文件来调用）：
# g++ -o testmain main.cpp
# python main.py