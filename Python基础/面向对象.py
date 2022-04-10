# Python3 面向对象

# 类对象
# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#     def f(self,a):                    
#         return 'hello world {}'.format(a)
# # 实例化类
# x = MyClass()   #创建一个空对象
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f(1))
# # # 无括号对象与有括号对象区别
# class aa:
#     def c(c):
#         print("aa{}".format(c));
# # aa.c(1)             #无括号对象可以直接传参给函数
# # 有括号参数
# class bb:
#     def c(c):         #有括号对象不能传参但是可以直接使用函数
#         print("bb");
# bb().c()   #不能传参否则报错


# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
# class test:
#     def __init__(self):       #构造函数第一个参数（self）是必加的类似this表示自身也就是实例其他可以作为传参
#         print('1111')
# x = test()
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r, x.i)   # 输出结果：3.0 -4.5
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self,在c的话可以单做this来用
# class Test:
#     def prt(self,q):
#         print(self)
#         print(self.__class__,q)     
# #self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。self 不是 python 关键字，可以任意命名只要在函数里有一个为代表实例的参数变量就行了
# t = Test()
# t.prt(1)
#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问，在py一般私有属性都是以__开头
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。%d测试" %(self.name,self.age,self.__weight))
#         # print("%s 说: 我 %d 岁。" %(self.name,self.age,self.q))
# # 实例化类
# p = people('runoob',10,30)
# p.speak()
# # print(p.__weight)   #因为私有变量所以无法被访问

# # 类继承
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
# s = student('ken',10,60,3)
# s.speak()
# #另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
# #多重继承
# class sample(speaker,student):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
# test = sample("Tim",25,80,4,"Python")
# test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法，如果是自身的话优先选择自己的

# 方法重写,如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法(相同名称的函数)
# class Parent:        # 定义父类
#    def myMethod(self):
#       print ('调用父类方法')
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print ('调用子类方法')
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
# super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法，super() 函数是用于调用父类(超类)的一个方法。

# 类属性与方法
# 类的私有属性：__attr两个下划线开头，声明该属性为私有，在类内部的方法中使用时 self.__attr。
# 类的方法：在类的内部定义类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
# 类的私有方法：__func：两个下划线开头，跟私有属性差不多只能在类的内部调用 。

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
#     def __init__(self, name, url):
#         self.name = name       # public
#         self.__url = url   # private
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print (self.__secretCount)
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#     def __foo(self):          # 私有方法
#         print('这是私有方法')
#     def foo(self):            # 公共方法
#         print('这是公共方法')
#         self.__foo()
# counter = JustCounter('菜鸟教程', 'www.runoob.com')
# print (counter.publicCount)
# counter.count()
# counter.count()
# counter.who()        # 正常输出
# counter.foo()        # 正常输出
# # counter.__foo()      # 报错
# # print (counter.__secretCount)  # 报错，实例不能访问私有变量

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 运算符重载，Python同样支持运算符重载，我们可以对类的专有方法进行重载
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
#    def __str__(self):                  #此类为类专有方法
#       return 'Vector (%d, %d)' % (self.a, self.b)
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)

# 作用域，因为python的特性局部变量和全局变量互相在通常情况下是不能互相访问的所以：当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。其实就类似于引用
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明，表示想访问外部（全局）变量
#     print(num) 
#     num = 123
#     print(num)
# fun1()
# print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()


