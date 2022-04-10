# Python3 基本数据类型
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# counter = 100          # 整型变量
# miles   = 1000.0       # 浮点型变量
# name    = "runoob"     # 字符串
# #多个变量赋值
# a = b = c = 1
# print (counter,miles,name+"\n")
# print (a,b,c)

# 标准数据类型
# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# Number（数字）
# Python3 支持数字(Number)类型: int(整数)、float(布尔型)、bool(浮点数)、complex（复数）。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，python整型是没有限制大小的，可以当作 Long 类型使用。
# bool (布尔), 如 True,False。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j
# Python 数字数据类型用于存储数值。数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
# 在Python 3里，只有一种整数类型 int，表示为长整型内置的而type() 函数可以用来查询变量所指的对象类型。
# a, b, c, d = 20, 5.5, True, 4+3j;
# print(type(a), type(b), type(c), type(d))
#可以使用十六进制和八进制来代表整数
# number1 = 0xA0F;     #十六进制
# number2 = 0o37         #八进制
# print(number1,number2);
# Python 数字类型转换 :[int(x),float(x),complex(x)(将x转换到一个复数，实数部分为 x，虚数部分为 0。),complex(x, y)(将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。)]
# a = 1.0
# print(int(a));
# 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 列如：
#交互模式：
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06
# 数学常量 ：[pi(数学常量 pi（圆周率，一般以π来表示）),e(数学常量 e，e即自然常数（自然常数）)]
# 此外还可以用 isinstance 来判断
# a = 111;
# print(isinstance(a, int));
# isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# class A:
#     pass
# class B(A):
#     pass
# print(isinstance(A(), A))
# print(type(A()) == A)
# print(isinstance(B(), A))
# print(type(B()) == A)
# 当你指定一个值时这个对象就会被创建：
# var1 = 1
# var2 = 10
# 你也可以使用del语句删除一些对象引用。[  del var1[,var2[,var3[....,varN]]]  ]
# del var1
# print(var1)

##字符串(String)
# Python中的字符串用单引号 ' 或双引号 " （两者作用完全相同）括起来也可以使用三引号(''' 或 """)做为多行字符串，同时使用反斜杠 \ 转义特殊字符。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string，用 + 将字符串连在一起，用 * 表示复制当前字符串。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 不支持单字符类型所以没有单独的字符类型，单字符在 Python 中也是作为一个字符串使用，一个字符就是长度为 1 的字符串。
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如a[0] = 'm'会导致错误。
# Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
# word = '字符串'
# sentence = "这是一个句子。" + "111""12"
# paragraph = """这是一个段落，
# 可以由多行组成，多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。"""
# print(word);
# print(sentence);
# print(paragraph);
#实例
# str='123456789'
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始后的所有字符
# print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str * 2)             # 输出字符串两次
# print(str + '你好')         # 连接字符串
# print('------------------------------')
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# Python 字符串更新，截取字符串的一部分并与其他字段拼接(py是用截取的方法加字符串覆盖进行更改字符串的，与其他语言不同不是用赋值的方式更改字符串)
# var1 = 'Hello World!'
# print ("已更新字符串 : ", var1[0:-2] + 'Runoob!');
# Python字符串运算符
# +	      字符串连接	
# *	      重复输出字符串
# []	  通过索引获取字符串中字符
# [ : ]	  截取字符串中的一部分，遵循左闭右开原则，
# in	  如果字符串中包含给定的字符返回 True
# not in  如果字符串中不包含给定的字符返回 True	
# r/R	  原始字符串：所有的字符串都是直接按照字面的意思来使用(比如转义和特殊字符)，可大小写
# %	格式字符串
# a = "Hello"
# b = "Python"
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
# print( r'\n' )
# print( R'\n' )
# if( "H" in a) :
#     print("H 在变量 a 中")
# else :
#     print("H 不在变量 a 中")
# if( "M" not in a) :
#     print("M 不在变量 a 中")
# else :
#     print("M 在变量 a 中")
# print (r'\n')
# print (R'\n')
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))  #最后的[ % ]代表要以格式化输出或者不起效
# f-string，称之为字面量格式化字符串，是新的格式化字符串的语法。
# 百分号%格式化输出
# name = 'Runoob'
# print('Hello %s' % name)
# f-string输出，格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
# name = 'Runoob'
# print(f'Hello {name}')  # 替换变量
# print(f'{1+2}')         # 使用表达式
# w = {'name': 'Runoob', 'url': 'www.runoob.com'}
# print(f'{w["name"]}: {w["url"]}')
# x = 1
# print(f'{x+1=}')              #可以使用 = 符号来拼接运算表达式与结果

##List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型类似C++的数组理念。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式变量[头下标:尾下标] 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 与Python字符串不一样的是，列表中的元素是可以改变的
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表
# list[2] = 2001
# print (list[2])
# list.append('Baidu')    #可以使用 append() 方法来添加
# print (list)
# a = [1, 2, 3, 4, 5, 6]
# a[0] = 9
# del a[2]                #可以用del删除元素
# a[2:5] = [13, 14, 15]
# print(a);
# a[2:5] = []   # 将对应的元素值设置为 []
# print(a);
#小实例
# def reverseWords(input):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],  
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords=inputWords[-1::-1]
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#     return output
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)

##Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。元组中的元素类型也可以不相同
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
# tup = "a", "b", "c", "d"  # 不需要括号也可以
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组
# print(type(tup))
# tup1 = ()    # 创建空元组
# tup2 = (20,) # 元组中只包含一个元素时，需要在元素后面添加逗号 ,[ ，]否则括号会被当作运算符使用可能会被认为整型来处理
# print(type(tup2))
# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取，其实，可以把字符串看作一种特殊的元组。
# tup = (1, 2, 3, 4, 5, 6)
# print(tup[0])
# print(tup[1:5])
# 更新元组，元组中的元素值是不允许修改的会报错，但我们可以对元组进行连接组合，如下
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# # tup1[0] = 100          #修改元组元素操作是非法的。
# tup3 = tup1 + tup2
# print (tup3)
# 删除元组
# tup4 = ('Google', 'Runoob', 1997, 2000)
# del tup4
# print (tup4)

##Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 创建格式：[   parame = {value01,value02,...}   ] 或者 [     set(value)    ]
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Google'}
# print(sites)   # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)     # a 和 b 的差集
# print(a | b)     # a 和 b 的并集
# print(a & b)     # a 和 b 的交集
# print(a ^ b)     # a 和 b 中不同时存在的元素
# a = {x for x in 'abracadabra' if x not in 'abc'}        #集合支持集合推导式(Set comprehension)
# print(a);
# 集合的操作
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.add("Facebook")         # 添加元素
# print(thisset)
# thisset.update({1,3})           #另一个添加元素方法
# print(thisset)
# thisset.remove("Taobao")        #移除元素， 不存在会发生错误
# print(thisset)
# thisset.discard("Facebook")     #另一个删除元素的方法，不存在不会发生错误
# print(thisset)
# x = thisset.pop()               #随机删除集合中的一个元素，并输出删除的元素
# print(x)
# print(thisset)
# print(len(thisset))             #计算集合元素个数
# thisset.clear()                 #清空集合,返回一个空集合
##Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型，一种可变容器模型，且可存储任意类型对象。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型,在同一个字典中，键(key)必须是唯一的。但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值
# 构造函数 dict() 可以直接从键值对序列中构建字典如下
# print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
# print({x: x**2 for x in (2, 4, 6)})
# print(dict(Runoob=1, Google=2, Taobao=3))
# 删除字典元素
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del dict['Name'] # 删除键 'Name'
# dict.clear()     # 清空字典
# del dict         # 删除字典
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])