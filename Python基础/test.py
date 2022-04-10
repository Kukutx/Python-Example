## Python3编程

## 斐波纳契数列
a, b = 0, 1
while b < 1000:
    print(b, end=',')         #end 关键字,可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，
    a, b = b, a+b