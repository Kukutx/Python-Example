## Python3 输入和输出

# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
# s = 'Hello, Runoob'
# print(s)
# print(str(s))
# print(repr(s))
# print(str(1/7))
# x = 10 * 3.25
# y = 200 * 200
# s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
# print(s)
# #  repr() 函数可以转义字符串中的特殊字符
# hello = 'hello, runoob\n'
# hellos = repr(hello)
# print(hellos)
# # repr() 的参数可以是 Python 的任何对象
# print(repr((x, y, ('Google', 'Runoob'))))
# 两种方式输出一个平方与立方的表
# for x in range(1, 11):
#      print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')     #字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
#      # 注意前一行 'end' 的使用
#      print(repr(x*x*x).rjust(4))
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#  zfill(), 它会在数字的左边填充 0
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))
# str.format() 
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))                               #以默认的方式格式化字段填充
# print('{0}网址： "{1}!"'.format('菜鸟教程', 'www.runoob.com'))                             #用数字用于指向传入对象在 format() 中的位置，初始为0
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))                # 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))  # 如果有一个很长的格式化字符串, 同时不想将它们分开。最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值

# 旧式字符串格式化
# import math
# print('常量 PI 的值近似为：%5.3f。' % math.pi)

# 读取键盘输入,Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘
str = input("请输入：");
print ("你输入的内容是: ", str)
