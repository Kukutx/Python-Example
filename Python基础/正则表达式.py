# Python3 正则表达式
# 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
import re

# re.match函数 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# 函数语法：re.match(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功re.match方法返回一个匹配的对象，否则返回None。
# 可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
# group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com')) 
# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")

# re.search方法 扫描整个字符串并返回第一个成功的匹配
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
# line = "Cats are smarter than dogs"
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
# if searchObj:
#    print ("searchObj.group() : ", searchObj.group())
#    print ("searchObj.group(1) : ", searchObj.group(1))
#    print ("searchObj.group(2) : ", searchObj.group(2))
# else:
#    print ("Nothing found!!")
# re.match与re.search的区别，re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

# 检索和替换
# Python 的re模块提供了re.sub用于替换字符串中的匹配项。
# 语法：re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# flags : 编译时用的匹配模式，数字形式。
# phone = "2004-959-559 # 这是一个电话号码"
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print ("电话号码 : ", num)
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print ("电话号码 : ", num)

# repl 参数是一个函数，以下实例中将字符串中的匹配的数字乘于 2
# 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 语法：re.compile(pattern[, flags])
# pattern : 一个字符串形式的正则表达式
# flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和' # '后面的注释
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print( m )
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print( m )
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print( m )                                        # 返回一个 Match 对象
print(m.group(0))   # 可省略 0
print(m.start(0))   # 可省略 0
print(m.end(0))     # 可省略 0
print(m.span(0))    # 可省略 0
# 在上面，当匹配成功时返回一个 Match 对象，其中：
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print( m )                            # 匹配成功，返回一个 Match 对象
# print(m.group(0))                            # 返回匹配成功的整个子串
# print(m.span(0))                             # 返回匹配成功的整个子串的索引
# print(m.group(1))                            # 返回第一个分组匹配成功的子串
# print(m.span(1))                             # 返回第一个分组匹配成功的子串的索引
# print(m.group(2))                            # 返回第二个分组匹配成功的子串
# print(m.span(2))                             # 返回第二个分组匹配成功的子串索引
# print(m.groups())                            # 等价于 (m.group(1), m.group(2), ...)
# # print(m.group(3))                            # 不存在第三个分组

# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# 语法：re.findall(pattern, string, flags=0)或pattern.findall(string[, pos[, endpos]])
# pattern 匹配模式。
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
# result1 = re.findall(r'\d+','runoob 123 google 456')
# pattern = re.compile(r'\d+')   # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# result3 = pattern.findall('run88oob123google456', 0, 10)
# print(result1)
# print(result2)
# print(result3)

# re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# it = re.finditer(r"\d+","12a32bc43jf3") 
# for match in it: 
#     print (match.group() )

# re.split方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：re.split(pattern, string[, maxsplit=0, flags=0])
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# re.split('\W+', 'runoob, runoob, runoob.')
# re.split('(\W+)', ' runoob, runoob, runoob.') 
# re.split('\W+', ' runoob, runoob, runoob.', 1) 
# re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割




#什么是正则表达式：正则表达式是使用单个字符串来描述，匹配一系列符合某个句法规则的字符串。 简单的理解，就是对字符串的检索匹配和处理
#python是通过re模块来提供正则表达式的
#方法1
# pattern=re.compile('hello')
# match = pattern.match('hello world')
# print (match.group())
#方法2
# word=re.findall('hello','hello word')
# print (word)

# #练习
# word="http://www.baidu.com python_1.1"
# # 一般字符 .
# key = re.findall('h.',word)
# print (key)

# # 一般字符 \
# key = re.findall('\.',word)
# print (key)

# key = re.findall('\d',word)
# print (key)

