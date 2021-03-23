#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 15:56 
# @Author : huangting 
# @File : 003_Square_root.py
# 平方根


# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16 = 4。语言描述为：根号下16 = 4。
# 以下实例为通过用户输入一个数字，并计算这个数字的平方根：

# author by : www.runoob.com

num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))
# 执行以上代码输出结果为：
# $ python test.py
# 请输入一个数字： 4
# 4.000的平方根为2.000

# 在该实例中，我们通过用户输入一个数字，并使用指数运算符 ** 来计算该数的平方根。
# 该程序只适用于正数。负数和复数可以使用以下的方式：

# author by : www.runoob.com

# 计算实数和复数平方根
# 导入复数数学模块

import cmath

num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
# 执行以上代码输出结果为：
# $ python test.py
# 请输入一个数字: -8
# -8的平方根为0.000 + 2.828j

# 该实例中，我们使用了cmath(complex math) 模块的sqrt()方法。



# 笔记
# 求复数的平方根。

import cmath

a = float(input("请输入一个实数字: "))
b = float(input("请输入一个虚数字: "))
num_sqrt = cmath.sqrt(complex(a, b))
print('{0:0.3f}+ {1:0.3f}j 8的平方根为 {2:0.3f}+{3:0.3f}j'.format(a, b, num_sqrt.real, num_sqrt.imag))



# 先假设我们会用input读取一个输入，它是一个字符串格式的，然后数字常用的是有小数点的浮点数float和整型int, 再考虑可能输入带负号，那么求出的平方根是复数complex, 所以可以分类讨论，下面的代码缺点是还没考虑到long型的。
# 可以依次输入 ： -2.56 -9 1.44 16来检验。

def sqrt():
    import cmath
    # # 计算实数和复数平方根# # 导入复数数学模块 isinstance(num ,  (float,int) )
    num = input('输入第一个数字：')
    if num.__contains__('-') and num.__contains__('.'):  # 负数、浮点数
        num_sqrt = cmath.sqrt(float(num))
        print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(float(num), num_sqrt.real, num_sqrt.imag))
    elif num.__contains__('-'):  # # 负数、整数
        num_sqrt = cmath.sqrt(int(num))
        print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(int(num), num_sqrt.real, num_sqrt.imag))
    else:
        if num.__contains__('.'):  # 非负数、浮点数 整数
            num_sqrt = float(num) ** 0.5
            print(' %0.3f 的平方根为 %0.3f' % (float(num), num_sqrt))
        else:  # # 非负数、整数
            num_sqrt = int(num) ** 0.5
            print(' %0.3f 的平方根为 %0.3f' % (int(num), num_sqrt))



# 异常报错+正数+负数

import cmath
try:
    num=float(input("请输入一个数字"))
except:
    print("输入的数字格式不正确,退出")
else:
    if num>=0:
        num_sqrt=num**0.5
        print(f"{num}的平方根是{num_sqrt:.3f}")
    else:
        num_sqrt=cmath.sqrt(num)
        print(f"{num}的平方根是{num_sqrt.real:.3f}+{num_sqrt.imag:.3f}j")
