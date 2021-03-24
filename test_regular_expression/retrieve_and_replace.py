#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 13:06 
# @Author : huangting 
# @File : retrieve_and_replace.py
# 检索和替换
import re

"""
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

语法：
re.sub(pattern, repl, string, count=0, flags=0)

参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
前三个为必选参数，后两个为可选参数。
"""

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
