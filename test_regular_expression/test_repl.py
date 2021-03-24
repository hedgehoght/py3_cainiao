#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 16:48 
# @Author : huangting 
# @File : test_repl.py
# repl 参数是一个函数

import re


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
