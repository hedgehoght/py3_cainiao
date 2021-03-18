#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:05 
# @Author : huangting 
# @File : 004_quadratic_equation.py
# 二次方程


# 以下实例为通过用户输入数字，并计算二次方程：

# author by : www.runoob.com

# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))

# x1 = ( -b + cmath.sqrt(b**2 -4*a*c) )/2*a
# x2 = ( -b - cmath.sqrt(b**2 -4*a*c) )/2*a
# 执行以上代码输出结果为：
# $ python test.py
# 输入 a: 1
# 输入 b: 5
# 输入 c: 6
# 结果为(-3 + 0j)和(-2 + 0j)

# 该实例中，我们使用了cmath(complex math) 模块的sqrt()方法来计算平方根。


# 笔记
import math

a, b, c = input("请输入3个数字(空格分隔)：").split()
a = float(a)
b = float(b)
c = float(c)
d = (b ** 2) - (4 * a * c)
if a == 0 and b == 0 and c == 0:
    print("有无穷个解")
elif d >= 0:
    x1 = ((-b - d) / (2 * a))
    x2 = ((-b + d) / (2 * a))
    print('结果为：%.2f,%.2f' % (x1, x2));
else:
    print("无解")
# 这样考虑到了无穷解与无解的情况哦




# 二次方程式 ax**2 + bx + c = 0
# 输入a、b、c
# 输出 x 的解
# x1=(-b+sqrt(b**2-4ac))/2a
# x2=(-b-sqrt(b**2-4ac))/2a

# 导入 cmath（复杂数学运算）模块
import cmath
import math

# 输入a、b、c
a = float(input("a的值："))
b = float(input("b的值："))
c = float(input("c的值："))

# 计算得到d
d = b * b - 4 * a * c
print("d的值：{}".format(d))

if d == 0:
    x = -b / 2 * a
    print("x的值{}".format(x));
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1的值{0}，x2的值{1}".format(x1, x2))
else:
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)




# 参考方法：
# coding=utf8
# 二次方程式 ax**2 + bx + c = 0
# 输入a、b、c
# 输出 x 的解
# x1=(-b+sqrt(b**2-4ac))/2a
# x2=(-b-sqrt(b**2-4ac))/2a

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


a = input('输入 a：')
b = input('输入 b：')
c = input('输入 c：')

if is_number(a) and is_number(b) and is_number(c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0 and b == 0:
        print('不是方程式，不需要解！')
    elif a == 0 and b != 0:
        x = -c / b
        print('为一次方程式，x 结果为：%.2f' % (x))
    elif a != 0 and b == 0:
        d = -c / a
        if d >= 0:
            x = math.sqrt(d)
            print('为一次方程式，x 结果为：%.2f' % (x))
        else:
            print('警告：该方程式无解！！！')
    elif a != 0 and b != 0:
        # 计算
        d = (b ** 2) - (4 * a * c)
        # print(d, math.sqrt(d))
        # 只有>=0的数才能开平方
        if d >= 0:
            x1 = (-b - math.sqrt(d)) / (2 * a)
            x2 = (-b + math.sqrt(d)) / (2 * a)
            print('结果为：x1 = %.2f,x2 = %.2f' % (x1, x2))
        else:
            print('警告：该方程式无解！！！')
    else:
        print('error')
else:
    print('请输入数字类型！！！')




# 参考方法：
# 求二次方程的根
from cmath import sqrt

a = int(input('please input the number a： '))
b = int(input('please input the number b： '))
c = int(input('please input the number c： '))
d = (b ** 2) - 4 * a * c
# 方法一：if判别语句
if a == 0:
    print('the number a can not be zero!')
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    # ！！！！print('x1和x2的值分别为{:0.3f} 和 {:0.3f}'.format(x1,x2))会出现错误，因为复杂格式不允许零填充！！！
    print('the values of x1 and x2 are {:.3f} and {:.3f}'.format(x1, x2))
# 方法二：用异常来进行处理
try:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print('the values of x1 and x2 are {:.3f} and {:.3f}'.format(x1, x2))
except ZeroDivisionError:
    print('the number a can not be zero!')




# 写了个比较完整的一元二次方程判断，实数根，复数根，提醒用户输入数字类数据......
import os
import math
import cmath


def mx(a, b, c):
    mm = (b ** 2) - (4 * a * c)
    if mm > 0:
        print('此函数有两个解')
        x1 = (-b + math.sqrt(mm)) / (2 * a)
        x2 = (-b - math.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f} 和 x={:.0f}".format(a, b, c, x1, x2))
    elif mm == 0:
        print('此方程只有一个解')
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f}".format(a, b, c, (-b + math.sqrt(mm)) / (2 * a)))
    elif mm < 0:
        x1 = (-b + cmath.sqrt(mm)) / (2 * a)
        x2 = (-b - cmath.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f} 和 x={:.0f}".format(a, b, c, x1, x2))
    else:
        print('无解')


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def panduan(xx):
    if is_number(xx) == True:
        return xx
    else:
        while is_number(xx) == False:
            print('不是数字，请再次输入')
            cc = input("请输入第一个数:")
            if is_number(cc) == True:
                break
        return ccprint('此程序用于计算一元二次方程解,请依次输入三个数')


zz = input("是否要开始计算:yes/no——:")
while zz == 'yes':
    a = float(panduan(input("请输入第一个数:")))
    b = float(panduan(input("请输入第二个数:")))
    c = float(panduan(input("请输入第三个数:")))
    mx(a, b, c)
    zz = input("是否还要继续计算:yes/no——:")
print('感谢使用。', end="")




# 分享一个自己写的练习题，定义了两个函数来分别实现获取用户输入以及解方程的功能，使得程序的可拓展性大大提高。代码如下：
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

import cmath


def get_para(para):
    """获取参数a, b, c的函数"""
    while True:
        try:
            number = float(input('请输入{}:'.format(para)))
            if para == 'a' and number == 0:
                print('a不能等于0!\n')
                continue
        except ValueError:
            print('请输入一个实数!\n')
            continue
        else:
            break
    return number


def solve(a, b, c):
    """解方程的函数"""
    d = b * b - 4 * a * c
    if d < 0:  # 复数解
        sol_1 = (-b + cmath.sqrt(d)) / (2 * a)
        sol_2 = (-b - cmath.sqrt(d)) / (2 * a)
    else:  # 实数解
        sol_1 = (-b + d ** 0.5) / (2 * a)
        sol_2 = (-b - d ** 0.5) / (2 * a)
    print('方程的两个解为:\n{}\n{}'.format(sol_1, sol_2))


print('-' * 60)
print('求解二次方程式 ax**2 + bx + c = 0 '.center(50))
print('-' * 60)
print('请提供a, b, c的值(a, b, c为实数，a ≠ 0)'.center(50))
print('-' * 60)

while True:
    a = get_para('a')
    b = get_para('b')
    c = get_para('c')
    solve(a, b, c)
    active = input('\n是否继续？(y/n): ')
    if active == 'n':
        break





# 综合上述笔记，自己写的练习题。考虑了特殊字符转换float的情况：
import cmath


def mx(a, b, c):
    if a == 0:
        if b == 0:
            print('不是方程')
            return
        else:  # b != 0
            print('一次方程 {} * x + {} = 0 的解为：\n x = {:.3f}'.format(b, c, -c / b))
            return
    else:  # a != 0
        print("二次方程{}x^2+{}x+{} = 0 的解为：".format(a, b, c))
        mm = (b ** 2) - (4 * a * c)
        if mm != 0:
            if mm < 0: print("无实数解")
            x1 = (-b + mm ** 0.5) / (2 * a)
            x2 = (-b - mm ** 0.5) / (2 * a)
            print("x1 = {0:.3f}".format(x1))
            print("x2 = {0:.3f}".format(x2))
        else:  # mm == 0
            x1 = -b / (2 * a)
            print("x1 = x2 = {0:.3f}".format(x1))


def is_number(s):
    try:
        float(s)

        if s in ['inf', 'infinity', 'INF', 'INFINITY', 'True', 'NAN', 'nan', 'False',
                 '-inf', '-INF', '-INFINITY', '-infinity', 'NaN', 'Nan']:
            return False
        else:
            return True
    except ValueError:
        return False


def panduan(xx):
    if is_number(xx) == True:
        return xx
    else:
        while is_number(xx) == False:
            print('不是数字，请再次输入')
            xx = input("请重新输入数:")
            if is_number(xx) == True:
                return xx


def 一元二次方程求解_复数():
    '''

1.a= 0
    1.1 b=0:不是方程
    1.2 b!=0 一次方程
2.a!= 0 :二次方程
    2.1 b^2-4ac > 0: 两个不同实数解
    2.2 b^2-4ac = 0: 两个相同解
    2.1 b^2-4ac < 0: 两个不同虚数解
    '''

    zz = input("是否要开始计算:y/n——:")
    while zz == 'Y' or zz == "y":
        a = float(panduan(input("请输入第一个数:")))
        b = float(panduan(input("请输入第二个数:")))
        c = float(panduan(input("请输入第三个数:")))
        mx(a, b, c)
        zz = input("是否还要继续计算:y/n——:")
    print('感谢使用。', end="")
# 一元二次方程求解_复数()





# 参考：
# 一元二次方程
import math

a = float(input("请输入系数a:"))
b = float(input("请输入系数b:"))
c = float(input("请输入常数c:"))
d = (b ** 2) - (4 * a * c)
d_sqrt = d ** 0.5
if d == 0:
    sol_1 = (-b - math.sqrt(d)) / (2 * a)
    sol_2 = (-b + math.sqrt(d)) / (2 * a)
    print("此方程有两个相等的实数根，它们为：{0:0.3f},{1:0.3f}".format(sol_1, sol_2))
elif d > 0:
    sol_1 = (-b - math.sqrt(d)) / (2 * a)
    sol_2 = (-b + math.sqrt(d)) / (2 * a)
    print("此方程有两个不相等的实数根，它们为：{0:0.3f},{1:0.3f}".format(sol_1, sol_2))
if d < 0:
    sol_1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol_2 = (-b + cmath.sqrt(d)) / (2 * a)
    print("此方程没有实数根，但有两个共轭复根，它们为：{0:0.1f}+{1:0.3f}i,{2:0.1f}+{3:0.3f}i"
          .format(sol_1.real, sol_1.imag, sol_2.real, sol_2.imag))
