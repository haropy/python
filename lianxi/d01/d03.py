# -*- coding: utf-8 -*-
# 分支结构
# @Time    : 2019/11/13 21:12
# @Author  : haropy
# 1.用户身份验证
# username = input("请输入用户名：")
# password = input("请输入用户名：")
# if username == 'admin' and password == '123456':
#     print("登陆成功")
# else:
#     print("登陆失败")


"""
2.分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# x = float(input("请输入x:"))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print("f(%.2f)=%.2f" % (x, y))

"""
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""

# x = float(input("请输入x:"))
# if x > 1:
#     y = 3 * x - 5
# else :
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print("f(%.2f)=%.2f" % (x, y))


# e1. 英制单位英寸与公制单位厘米互换
# value = float(input("请输入长度："))
# unit = input("请输入单位：")
# if unit == 'in' or unit == '英寸':
#     print("%f英寸 = %f厘米" % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print("%f厘米 = %f英寸" % (value, value / 2.54))
# else:
#     print("请输入有效单位")

# e2.百分制成绩转换为等级制成绩
# score = float(input("请输入成绩："))
# if score >= 90:
#     grade = "A"
# elif score > 80:
#     grade = "B"
# elif score > 70:
#     grade = "C"
# else:
#     grade = "D"
# print("对应的等级是：", grade)

# e3 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' % (area))
else:
    print('不能构成三角形')
