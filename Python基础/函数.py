## Python3 函数

# 定义一个函数
# 函数定义是以 def 关键词开头，然后函数名和圆括号 ()。   def main():
# (括号中间可以传入参数和自定义变量)，圆括号之间可以用于定义参数。
# 函数内容也就是代码块必须以冒号 : 起始，并且缩进区分代码块范围。
# return [表达式] 结束函数，返回一个值给调用方，不带表达式的 return 相当于返回 None。
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# a = 4
# b = 5
# print(max(a, b))

# 参数传递
# 在 python 中，类型属于对象，变量是没有类型的
# 在代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
# 可更改(mutable)与不可更改(immutable)对象：
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
# python 函数的参数传递：
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

#可写函数说明
# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print ("名字: ", name)
#    print ("年龄: ", age)
#    return
# #调用printinfo函数
# printinfo( age=50, name="runoob" )
# print ("------------------------")
# printinfo( name="runoob" )

# 加了 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vartuple)
# # 调用printinfo 函数
# printinfo( 70, 60, 50 )
# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
# def printinfo( arg1, **vardict ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vardict)
# # 调用printinfo 函数
# printinfo(1, a=2,b=3)

## 匿名函数,python 使用 lambda 来创建匿名函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print ("相加后的值为 : ", sum( 10, 20 ))
# print ("相加后的值为 : ", sum( 20, 20 ))