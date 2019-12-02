# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 15:43
# @Author  : haropy

"""
「 #测试技术面试题#

string="192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"

要求：返回一个IP数组，并并且按ip最后一位排序返回。 」
"""
import re
import socket
str="192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"

def get_ip(str):
    str_list = re.split('[?!]',str)
    for s in str_list:
        if s == '':
            str_list.remove(s)
    print (str_list)
    return str_list

def sort_ip(str_list):
    ip = sorted(str_list,key = lambda x: (int(x.split('.')[3])))
    print (ip)
    return ip

sort_ip(get_ip(str))