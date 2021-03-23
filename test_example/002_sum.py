#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 15:50 
# @Author : huangting 
# @File : 002_sum.py
# 数字求和

# author by : www.runoob.com

# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
# 执行以上代码输出结果为：
# 输入第一个数字：1.5
# 输入第二个数字：2.5
# 数字 1.5 和 2.5 相加结果为： 4.0

# 在该实例中，我们通过用户输入两个数字来求和。使用了内置函数 input() 来获取用户的输入，input() 返回一个字符串，所以我们需要使用 float() 方法将字符串转换为数字。
# 两数字运算，求和我们使用了加号 (+)运算符，除此外，还有 减号 (-), 乘号 (*), 除号 (/), 地板除 (//) 或 取余 (%)。更多数字运算可以查看我们的Python 数字运算。

# 我们还可以将以上运算，合并为一行代码：
print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
# 执行以上代码输出结果为：
# $ python test.py
# 输入第一个数字：1.5
# 输入第二个数字：2.5
# 两数之和为 4.0


# 笔记
# 尝试写了一个报错重新输入的处理处理:
while 1:
    x=input("请输入数字x的值")
    y=input("请输入数字y的值")
    try:
        sum=float(x)+float(y)
    except:
        print("输入的数字格式不正确,请重新输入")
        continue
    else:
        print(f"两个数字之和为{sum:.2f}")
        break
