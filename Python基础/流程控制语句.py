## Python3 条件控制
# if 语句
#Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
# 每个条件后面要使用[ : ]表示代码块直到遇到缩进或者下一条语句的冒号，使用缩进来划分代码块，相同缩进数的语句组成一个代码块。
# n=2;
# if n==1:
#     print(1);
# elif n<0:                   
#     print(2);
# else:
#     print(3);
#简单的小实例
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
# ### 退出提示
# input("点击 enter 键退出")

## Python3 循环语句
## while 循环
# while (1): print ('欢迎访问菜鸟教程!')              #如果语句简单的话可以在一行语句实现
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n,sum))
# while 循环使用 else 语句，如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")
## for 语句
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")
# range()函数,如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
# for i in range(5):
#     print(i)
#使用range指定区间的值
# for i in range(5,9) :
#     print(i)
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
# for i in range(0, 10, 3) :
#     print(i)
# for i in range(-10, -100, -30) :
#     print(i)
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])
# break 和 continue 语句可调整流程控制
# for letter in 'Runoob':     # 第一个实例
#    if letter == 'b':
#       break
#    print ('当前字母为 :', letter)
# var = 10                    # 第二个实例
# while var > 0:              
#    print ('当期变量值为 :', var)
#    var = var -1
#    if var == 5:
#       break
# print ("Good bye!")
##pass 语句，Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
# while True:
#     pass  # 等待键盘中断 (Ctrl+C)
# class MyEmptyClass:
#     pass                  #最小的类
# for letter in 'Runoob': 
#    if letter == 'o':
#       pass
#       print ('执行 pass 块')
#    print ('当前字母 :', letter)
# print ("Good bye!")