#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/19 14:48 
# @Author : huangting 
# @File : number_type_change.py
# 数字类型转换

"""
int(x) 将x转换为一个整数。

float(x) 将x转换到一个浮点数。

complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。

complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
"""

a = 11.11
print(int(a))
print(float(a))
print(complex(a))
print(complex(a, 2))
