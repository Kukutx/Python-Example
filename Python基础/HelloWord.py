'''
#!/usr/bin/python3                                    ##Linux的编译配置如win无需此配置
# -*- coding: utf8 -*-                                ##设置编码格式            
# 可执行此命令在命令行运行py格式语句：[python3 hello.py  /  python hello.py]
# 也可以用python的交互式编程即命令行命令编程[python],退出可以输入quit(),exit()
# Python理念为一切皆对象
'''

###Python基础知识

##基本输出语句Print
#print("Hello, World!");
# str;                            #变量在使用前必须先"定义"（即赋予变量一个值）
x="a"
y="b"
# 换行输出
print( x )
print( y )
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
print( x, y)

##python关键词                    #Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字
# import keyword
# print(keyword.kwlist);

##python注释
# 单行注释以#开头
# 多行注释可['''] 和 ["""]开头到结尾

##python行与缩进                  
##python是使用缩进来表示代码块，不需要使用大括号 {} 。缩进的空格数是可变的，但同一个代码块的语句必须相同的缩进空格数,如果缩进空格数不一致，会导致错误
# if True:
#     print ("Answer");
#     print ("True");
# else:
#     print ("Answer");
#     print ("False");    
##在交互式编程里当键入一个多行结构时，续行是必须的如下 if 语句：
'''
>>> flag = True
>>> if flag :
...     print("flag 条件为 True!");
... 

'''

## Python多行语句                 #Python 通常一行写完一条语句，如果语句很长可以使用 \ 来实现多行语句。在 [], {}, () 中的多行语句，不需要使用 \
# total = 1 + \
#         2 + \
#         3;
# print(total);
# total = ['item_one', 'item_two', 'item_three',
#         'item_four', 'item_five'];





##同一行显示多条语句              #可用交互式编程
# import sys; x = 'runoob'; sys.stdout.write(x + '\n');

##import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:');
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path);
# #导入特定的成员
# from sys import argv,path  
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
