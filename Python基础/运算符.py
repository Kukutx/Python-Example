## Python3 运算符
# Python 语言支持以下类型的运算符:
# 算术运算符 : +,-,*,/,%,**(次方),//（取整除）
# 比较（关系）运算符 : ==,!=,<,>,<=,>=
# 赋值运算符 : =,+=,-=,*=,/=,%=,**=,//=,:=(海象运算符，可在表达式内部为变量赋值)
# 位运算符  : &,|,^,~,<<,>>
# 逻辑运算符  : and,or,not
# 成员运算符  : in(如果在指定的序列中找到值返回 True，否则返回 False。),not in (如果在指定的序列中没有找到值返回 True，否则返回 False。)
# 身份运算符 (身份运算符用于比较两个对象的存储单元) : is(is 是判断两个标识符是不是引用自一个对象[注意在py数字也是对象，一切皆对象]),is not(is not 是判断两个标识符是不是引用自不同对象)
# 运算符优先级 :
'''
**
~ + -	
* / % //	
+ -	
>> <<	
&	
^ |	
<= < > >=	
== !=	
= %= /= //= -= += *= **=	
is is not	
in not in	
not and or

'''

# 成员运算符
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ]
# if ( a in list ):
#    print ("1 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("1 - 变量 a 不在给定的列表中 list 中")
# if ( b not in list ):
#    print ("2 - 变量 b 不在给定的列表中 list 中")
# else:
#    print ("2 - 变量 b 在给定的列表中 list 中")
# # 修改变量 a 的值
# a = 2
# if ( a in list ):
#    print ("3 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("3 - 变量 a 不在给定的列表中 list 中")

# 身份运算符
# a = 20
# b = 20
# if ( a is b ):                      #x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
#    print ("1 - a 和 b 有相同的标识") 
# else:
#    print ("1 - a 和 b 没有相同的标识")
# if ( id(a) == id(b) ):               #id() 函数用于获取对象内存地址。
#    print ("2 - a 和 b 有相同的标识")
# else:
#    print ("2 - a 和 b 没有相同的标识")
# # 修改变量 b 的值
# b = 30
# if ( a is b ):
#    print ("3 - a 和 b 有相同的标识")
# else:
#    print ("3 - a 和 b 没有相同的标识")
# if ( a is not b ):                    #x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
#    print ("4 - a 和 b 没有相同的标识")
# else:
#    print ("4 - a 和 b 有相同的标识")
