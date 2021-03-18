#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 17:01 
# @Author : huangting 
# @File : 018_mul_table.py
# 九九乘法表


# 以下实例演示了如何实现九九乘法表：

# author by : www.runoob.com

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()
# 执行以上代码输出结果为：
# 1x1=1
# 1x2=2    2x2=4
# 1x3=3    2x3=6    3x3=9
# 1x4=4    2x4=8    3x4=12    4x4=16
# 1x5=5    2x5=10    3x5=15    4x5=20    5x5=25
# 1x6=6    2x6=12    3x6=18    4x6=24    5x6=30    6x6=36
# 1x7=7    2x7=14    3x7=21    4x7=28    5x7=35    6x7=42    7x7=49
# 1x8=8    2x8=16    3x8=24    4x8=32    5x8=40    6x8=48    7x8=56    8x8=64
# 1x9=9    2x9=18    3x9=27    4x9=36    5x9=45    6x9=54    7x9=63    8x9=72    9x9=81
# 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。




# 笔记
# 乘法表左边的数要比右边的小，如下实例:
# !/usr/bin/python3

class multiplicationTable():
    def paint(self, n=9):
        for row in range(1, n + 1):
            for col in range(1, row + 1):
                print("{1}x{0}={2}\t".format(row, col, row * col), end='')
            print();


table = multiplicationTable()
table.paint()
# table.paint(10) #打印 "10x10" 的乘法表




# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        if i == j:
            print('{1}×{0}={2}'.format(i, j, i * j))
        else:
            print('{1}×{0}={2}'.format(i, j, i * j), end='\t')
# 这样写可以有效去除每一行的最后一个空格, 输出如下：




# 一句话输出99乘法表，可以参考一下：
print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)))




# 参考：
for i in range(1, 10):
    for j in range(1, i):
        print
        "%dx%d=%d" % (j, i, j * i),
    print



# 用列表生成器打印九九乘法表:
# >>> print '\n'.join(['\t'.join(['%d * %d = %d' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)])


# 分享给像我这种门外汉，稍微好理解一些，Python3支持中文变量真好。
for 行 in range(1, 10):
    for 列 in range(1, 行 + 1):  # 内循环中，确保列 <= 行。
        print("{}*{}={}\t".format(列, 行, 列 * 行), end="")  # 确保同一行内容连续
    print()  # 另起一行！！！

input()  # 防止程序一闪而过，不在编译器中也能使用
