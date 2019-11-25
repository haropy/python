# -*- coding: utf-8 -*-
# 循环结构
# @Time    : 2019/11/13 21:12
# @Author  : haropy

# 1 for-in 循环 明确的知道循环次数或者要对一个容器进行迭代
"""
用for循环实现1~100求和
"""
# sum = 0
# for x in range(1, 101):
#     sum += x;
# print(sum)

"""
用for循环实现1~100的偶数求和
"""
# sum = 0
# for x in range(2, 101,2):
#     sum += x;
# print(sum)

"""
用for循环实现1~100的偶数求和
"""
# sum = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x;
# print(sum)


# while循环
# 我们要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
# while循环通过一个能够产生或转换出bool值的表达式来控制循环
"""
猜字游戏
"""
# import random
#
# answer = random.randint(1, 100)
# print(answer)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number > answer:
#         print('大一点')
#     elif number < answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

"""
输出乘法口诀
"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

# e1 输入一个正整数判断是不是素数
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

