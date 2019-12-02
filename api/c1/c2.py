# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 18:01
# @Author  : haropy
# 4 其他流程控制工具

# 4.1 if 语句
# x = int(input("Please enter an integer:"))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# 4.2 for语句 对任意序列进行迭代（例如列表或字符串）
# words = ['cat','window','defenestrate']
# for w in words:
#     print(w,len(w))

# 在遍历同一个集合时修改该集合的代码可能很难获得正确的结果。通常，更直接的做法是循环遍历该集合的副本或创建新集合：
# Stragey:Iterate over a cpoy
# for user,status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Stragey:Create a new collection
# active_users = {}
# for user,status in users.items():
#     if status == 'active':
#         active_users[user] = status

# 4.3 range()函数 遍历一个数字序列，内置函数range（）会派上用场。它生成算术级数：
# for i in range(1, 5):
#     print(i)

# a = ['Mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])

# for i, a in enumerate(['Mary', 'had', 'a', 'little', 'lamb']):
#     print(i, a)

# print(range(10))
# range() 所返回的对象会在你迭代它时基于所希望的序列返回连续的项，
# 但它没有真正生成列表，这样就能节省空间。这样的对象为iterable。例子
# print(sum(range(4)))

# 返回可迭代对象以及可迭代对象作为参数的函数。从一个指定范围内获取一个列表。
print(list(range(4)))