# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 18:32
# @Author  : haropy

a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True

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
"""
将华氏温度转换为摄氏温度
"""
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度=%.1f摄氏度' % (f, c))

"""
输入圆的半径计算计算周长和面积
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

"""
输入年份判断是不是闰年
"""
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)
