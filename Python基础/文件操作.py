# File,OS
# Python3 File(文件) 方法
# -*- coding: UTF-8 -*-

# 读和写文件
# open() 将会返回一个 file 对象,open(filename, mode),filename：要访问的文件名。mode：决定了打开文件的模式：只读，写入，追加等
# 完整的语法格式:open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数说明:
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# 打开一个文件
f = open("./filetmp/foo.txt", "r+",-1,'utf8')        #创建文件对象

# f.write() 将 string 写入到文件中, 然后返回写入的字符数
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )         
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)

# f.read() # 读取一个文件的内容,f.read(size),size要读取的数量
# str = f.read()
# print(str)

# f.readline(),会从文件中读取单独的一行。
# str2 = f.readline()
# print(str2)

# f.readlines()将返回该文件中包含的所有行。
# str3 = f.readlines()
# print(str3)

# 另一种方式是迭代一个文件对象然后读取每行
# for line in f:
#     print(line, end='')

f.close()       # 关闭文件对象

####如果想深入学习的话可以参考 Python3 OS模块  文件/目录方法