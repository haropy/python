# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 18:36
# @Author  : haropy
# 构造程序逻辑

"""
1.寻找水仙花数
"""
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

"""
2.正整数的反转
"""
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
3.百钱百鸡
"""
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))

"""
4.Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""
# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的总资产是：', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注：'))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money += debt
#         elif current == first:
#             print('玩家胜')
#             money -= debt
#         else:
#             needs_go_on = True
# print('你破产了，游戏结束！')

# e1 生成斐波那契数列的前20个数
n = int(input('输入n：'))
a = 1
b = 1

a = a + b
b = a
print(a)

# e2 找出10000以内的完美数

# e3 输出100以内所有的素数