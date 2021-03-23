#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:11 
# @Author : huangting 
# @File : 005_area_of_triangle.py
# 计算三角形的面积


# 以下实例为通过用户输入三角形三边长度，并计算三角形的面积：

# author by : www.runoob.com


a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)
# p = (a+b+c) /2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))

# 执行以上代码输出结果为：
# $ python test.py
# 输入三角形第一边长: 5
# 输入三角形第二边长: 6
# 输入三角形第三边长: 7
# 三角形面积为 14.70




# 笔记
# 加上判断三角形能否构成的条件：
# 实例四：计算三角形面积

a = float(input('输入三角形第一边长：'))
b = float(input('输入三角形第二边长：'))
c = float(input('输入三角形第三边长：'))
while a + b < c or a + c < b or b + c < a:
    print('输入的边构不成三角形，请重新输入！')
    a = float(input('输入三角形第一边长：'))
    b = float(input('输入三角形第二边长：'))
    c = float(input('输入三角形第三边长：'))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为：%0.2f' % area)




# 参考方法：
# 计算三角形面积
while (True):
    triangle = input('输入三角形三边(如10,6,8):')
    sides = [int(side) for side in triangle.split(',')]
    a, b, c = sides

    # 判断输入的三角形是否合法
    if a + b > c and a + c > b and b + c > a:
        s = a * b * (1 - ((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) ** 2) ** 0.5 / 2
        print('三角形({0[0]},{0[1]},{0[2]})的面积是：{1}'.format(sides, s))
        break
    else:
        print('三角形不合法')




# Python3下测试：
while True:
    triangle = input('输入三角形三边(如10,6,8):')
    sides = [float(side) for side in triangle.split(',')]
    a, b, c = sides

    # 判断输入的三角形是否合法
    if a + b > c and a + c > b and b + c > a:
        l = (a + b + c) / 2
        s = (l * (l - a) * (l - b) * (l - c)) ** 0.5
        print('三角形({0[0]},{0[1]},{0[2]})的面积是：{1:.2f}'.format(sides, s))
        break
    else:
        print('三角形不合法')




# 参考方法：
# 通过用户输入三角形三边长度，并计算三角形的面积
# 已知三角形三边a,b,c，则
# （海伦公式）（p=(a+b+c)/2）
# S=sqrt[p(p-a)(p-b)(p-c)]
# =sqrt[(1/16)(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
# =1/4sqrt[(a+b+c)(a+b-c)(a+c-b)(b+c-a)]

import math
import unicodedata


# 定义函数判断输入数据是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.digit(s)  # digit 把一个合法的数字字符串转换为数字值
        return True
    except (TypeError, ValueError):
        pass
    return False


def calculate(a, b, c):
    if is_number(a) and is_number(b) and is_number(c):
        a = float(a)
        b = float(b)
        c = float(c)
        if a > 0 and b > 0 and c > 0:
            while a + b <= c or a + c <= b or b + c <= a:
                print("输入的边长无法构成三角形！！！")
                a = input('输入三角形边长a: ')
                b = input('输入三角形边长b: ')
                c = input('输入三角形边长c: ')
                calculate(a, b, c)
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("三角形面积为：%0.2f" % area)
        else:
            print("三角形的边长必须大于0，请输入大于0的数！！！")
    else:
        print('请输入数字类型！！！')


a = input('输入三角形边长a: ')
b = input('输入三角形边长b: ')
c = input('输入三角形边长c: ')
calculate(a, b, c)




# 判断输入数据是否能组成三角形:
def isTriangle(a, b, c):
    flag = 1
    if (a + b > c and a + c > b and b + c > a):
        if (a == b == c):
            print("输入数据构成的三角形为等边三角形")
        elif (a == b or a == c or b == c):
            print("输入数据构成的三角形为等腰三角形")
        else:
            print("输入数据构成的三角形为普通三角形")
        flag = 1
    else:
        # print("输入数据不能构成三角形，请重新输入数据！")
        flag = 0
    return flag


# 计算三角形的面积
def triangleArea(a, b, c):
    if (isTriangle(a, b, c) == 1):
        # 计算半周长
        s = (a + b + c) / 2
        # 计算面积
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('三边边长分别为{0} {1} {2}的三角形的面积为{3:.2f}'.format(a, b, c, area))
    else:
        print("输入数据不能构成三角形，请重新输入数据！")
        a = float(input("请输入三角形第一条边长的数据："))
        b = float(input("请输入三角形第二条边长的数据："))
        c = float(input("请输入三角形第三条边长的数据："))
        triangleArea(a, b, c)


a = float(input("请输入三角形第一条边长的数据："))
b = float(input("请输入三角形第二条边长的数据："))
c = float(input("请输入三角形第三条边长的数据："))
triangleArea(a, b, c)




# 所以说不用专门写一个函数判断是否为数字。
import math


def calculate():
    while True:
        while True:
            try:
                triangle = input('Length, Width, Height:(split by spaces)').split()  # 一次输入3个参数
                a, b, c = [float(i) for i in triangle]  # 分割3个参数
                break
            except ValueError:  # 判断是否为数字
                print('请输入数字类型！！！')

        if a > 0 and b > 0 and c > 0:
            if a + b <= c or a + c <= b or b + c <= a:
                print("输入的边长无法构成三角形！！！")
            else:
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print('长为{0},宽为{1},高为{2}的三角形面积为{3}'.format(a, b, c, area))
                break
        else:
            print('三角形的边长必须大于0，请输入大于0的数！！！')


if __name__ == '__main__':
    calculate()




# 写个简单的, 代码可读性是python追求的原则:
import math

# 可以不导入模块,像例子那样写 x**0.5
while True:
    print("请先输入三角形的三边长a,b,c")
    try:
        # 输入字符串会非法,提示重新输入
        a = float(input("请输入边长a:"))
        b = float(input("请输入变成b:"))
        c = float(input("请输入边长c:"))
    except ValueError:
        print("您输入的不是一个数字无法计算三角形面积,请重新输入正确的数字")
    else:
        # 判断三边的边长能否构成一个三角形
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("三角形的面积为:{0:.3f}".format(s))
        else:
            print("输入的三边构不成三角形")




# sorted是在网上看到的，分享一下:
import math

judge = True
while judge:
    a, b, c = sorted(eval(input('请输入三边长【以逗号隔开】：')))  # 给三边排序，避免后面的分类
    if a > 0 and b > 0 and c > 0:
        if c < b + a:  # 因为sorted的结果是 a>b>c,所以只需一个判断就可
            p = (a + b + c) / 2
            S = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print('三角形的面积是：%.3f' % S)
            judge = False
        else:
            print('三边不能构成三角形，请重新输入三个正数，用逗号隔开')
            print()  # 上下两次循环隔开，没那么密集，下同
    else:  # 可以排除其他误输入类型
        print('输入有误，请输入三个正数，用逗号隔开。')
        print()
        continue
