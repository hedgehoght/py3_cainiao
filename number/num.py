#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/19 14:43 
# @Author : huangting 
# @File : num.py
# 数字(Number)

var1 = 10
var2 = 20
print(var1,var2)

# 删除数字对象的引用
del var1,var2
# print(var1,var2)

"""
Python 支持三种不同的数值类型：

整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
"""

number = 0xA0F # 十六进制
print(number)
number=0o37 # 八进制
print(number)
