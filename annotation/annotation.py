#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 17:25 
# @Author : huangting 
# @File : annotation.py
# 注释

# 单行注释

# 多行注释
# 1 单引号（'''）

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
print("Hello, World!")


# 双引号（"""）

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""
print("Hello, World!")




# 笔记
# 以下实例我们可以输出函数的注释：
def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)
# 输出结果为：
# 这是文档字符串



# 三个双引号赋值给字符串变量时，表示一种字符串的特殊写法。
# >>> str="""I
# ... want
# ... you"""
# >>> str
# 'I\nwant\nyou'
# >>> print(str)
# I
# want
# you
# 单引号在这里的用法与双引号相同。




# (to一楼）当函数中有语句的时候，是无法输出函数的注释的:
def a():
    a=1
    '''这是文档字符串'''
    pass
print(a.__doc__)
# 输出结果为：None

# 以下这种方式可以，所以注释应该放在函数的第一行：
def a():
    '''这是文档字符串'''
    a = 1
    pass
print(a.__doc__)
# 这是文档字符串
