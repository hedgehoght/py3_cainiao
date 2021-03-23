#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:57 
# @Author : huangting 
# @File : 017_factorial.py
# 阶乘实例

s = 1


def jiecheng(x):
    global s
    for i in range(1, x + 1):
        s = s * i
    return s


n = int(input('输入整数n：'))
if n < 0:
    print('输入值错误')
elif n == 0:
    print('0的阶乘为0')
else:
    jiecheng(n)
    print('%d 的阶乘是 %d' % (n, s))




# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n != 1×2×3×...×n。

# author by : www.runoob.com

# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1

# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("%d 的阶乘为 %d" % (num, factorial))
# 执行以上代码输出结果为：
# 请输入一个数字: 3
# 3 的阶乘为 6



# 笔记
# 参考方法：
# !/usr/bin/python3

from functools import reduce

sum = reduce(lambda x, y: x * y, range(1, 7))
print(sum)



# 查了一下 math 库的帮助，发现自带阶乘函数。所以代码可以简洁一点。
# -*- coding: UTF-8 -*-

# Filename : factorial.py
# author : Pt

import math

num = int(input("请输入一个数字："))
if num < 0:
    print("负数是没有阶乘的！")
else:
    print("{0} 的阶乘为 {1}".format(num, math.factorial(num)))





# 递归实现
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1


while True:
    try:
        n = input("请输入一个数字(输入 q 退出):")
        if n == "q":
            break
        n = int(n)
        if n < 1:
            raise ValueError
        x = factorial(n)
        print(x)
    except ValueError:
        print("不是一个正数")



# 学渣观点：
# 1.递归实现不可取
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1


while True:
    try:
        n = input("请输入一个数字(输入 q 退出):")
        if n == "q":
            break
        n = int(n)
        if n < 1:
            raise ValueError
        x = factorial(n)
        print(x)
    except ValueError:
        print("不是一个正数")
# 超过 1000 的阶乘计算后会报错:
# RecursionError: maximum recursion depth exceeded in comparison
# 报错提示：超过最大递归深度。
# 解决办法：可以修改递归深度的值，让它变大大一点。
# 代码看起来很好，但是有个致命问题，你试试看 1000 的阶乘，记得一个经典例题 IBM 出 1000 的阶乘，都说很容易，但是考虑过这数据的存储吗？递归做这种大数字计算感觉不怎么行了。而且有更加简单且有效的方法，python 的特点应该是自带的数学公式。
# 2.示例代码，和下面用阶乘函数的代码，实际操作 70000 的阶乘计算速度才受到一些影响，肉眼感觉相差不大。
# 3.入门python感觉，python最大的优势还是在于自带的数学计算式，代码的简洁，大数的计算，因此学python应尽可能用数学公式来码代码。 学渣观点，有疑问接受反驳，QQ：1017736803
