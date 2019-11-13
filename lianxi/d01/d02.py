# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 18:32
# @Author  : haropy
# 语言元素
"""
变量：
    整型
    浮点型
    字符串型
    布尔型
    复数型

变量命名：
    硬性规则：
    变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
    大小写敏感（大写的a和小写的A是两个不同的变量）。
    不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
    PEP 8要求：
    用小写字母拼写，多个单词用下划线连接。
    受保护的实例属性用单个下划线开头（后面会讲到）。
    私有的实例属性用两个下划线开头（后面会讲到）       
"""
# 1 使用变量保存数据并进行算术运算
# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True

# 2 使用type()检查变量的类型
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# 可以使用内置函数对变量类型进行转换。
# int():将一个数值或字符串转换成整数，可以指定进制。
# float():将一个字符串转换成浮点数。
# str():将指定的对象转换成字符串形式，可以指定编码。
# char():将整数转换成该编码对应的字符串（一个字符）。
# ord():将字符串（一个字符）转换成对应的编码（整数）。

"""
3 使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
# %占位符

# 4 运算符
# 运算符	描述
# [] [:]	下标，切片
# **	指数
# ~ + -	按位取反, 正负号
# * / % //	乘，除，模，整除
# + -	加，减
# >> <<	右移，左移
# &	按位与
# ^ |	按位异或，按位或
# <= < > >=	小于等于，小于，大于，大于等于
# == !=	等于，不等于
# is is not	身份运算符
# in not in	成员运算符
# not or and	逻辑运算符
# = += -= *= /= %= //= **= &= `	= ^= >>= <<=

"""
e1 将华氏温度转换为摄氏温度
"""
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度=%.1f摄氏度' % (f, c))

"""
e2 输入圆的半径计算计算周长和面积
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

"""
e3 输入年份判断是不是闰年
"""
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)
