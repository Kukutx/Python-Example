# Python3 模块
# 在前面的几个章节中我们基本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
# 文件名: using_sys.py
# import sys                                                    #import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# print('命令行参数如下:')
# for i in sys.argv:                                            #sys.argv 是一个包含命令行参数的列表。
#    print(i)
# print('\n\nPython 路径为：', sys.path, '\n')                   #sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

# import 语句,引用语句可以引用自定义源文件的方法或者标准库的方法
# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
# # 导入模块
# import support
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")

#from … import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间或者函数中
# from support import fib, fib2
# fib(500)
# from … import * 语句,把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明
# from support import*

# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想直到模块是否被引入，模块中的某一程序块不执行，
# 我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# 说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
# import support

# dir() 函数，内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
# import support, sys
# print(dir(support))

