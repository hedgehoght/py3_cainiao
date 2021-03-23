#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:24 
# @Author : huangting 
# @File : 009_swap_variable.py
# 交换变量

def exchange():
    global x1
    global x2
    tmp = x1
    x1 = x2
    x2 = tmp
    print('x1 = %f and x2 = %f' % (x1, x2))
    return (x1, x2)


x1 = float(input('enter x1 :'))
x2 = float(input('enter x2 :'))

exchange()
print('x1 = %f and x2 = %f' % (x1, x2))



# 以下实例通过用户输入两个变量，并相互交换：

# author by : www.runoob.com

# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
# 执行以上代码输出结果为：
# 输入 x 值: 2
# 输入 y 值: 3
# 交换后 x 的值为: 3
# 交换后 y 的值为: 2

# 以上实例中，我们创建了临时变量temp ，并将x的值存储在temp变量中，接着将y值赋给x，最后将temp赋值给变量。
# 不使用临时变量
# 我们也可以不创建临时变量，用一个非常优雅的方式来交换变量：
# x, y = y, x
# 所以以上实例就可以修改为：

# author by : www.runoob.com

# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x, y = y, x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
# 执行以上代码输出结果为：
# 输入 x 值: 1
# 输入 y 值: 2
# 交换后 x 的值为: 2
# 交换后 y 的值为: 1



# 笔记
# 不使用临时变量:
# -*- coding: UTF-8 -*-

# 用户输入
x = int(input('输入 x 值: '))
y = int(input('输入 y 值: '))

x = x + y
y = x - y
x = x - y

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))




# 异或形式：
# 交换变量
x = int(input('输入 X 值：'))
y = int(input('输入 Y 值：'))
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后的 X 值为：', x)
print('交换后的 Y 值为：', y)




# 乘法形式：
x=int(input('x='))
y=int(input('y='))
x=x*y
y=x/y
x=x/y
print('x='+str(int(x))+'\ny='+str(int(y)))
