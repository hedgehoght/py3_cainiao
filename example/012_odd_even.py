#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:38 
# @Author : huangting 
# @File : 012_odd_even.py
# 判断奇数偶数

# 以下实例用于判断一个数字是否为奇数或偶数：

# author by : www.runoob.com

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

num = int(input("输入一个数字: "))
if (num % 2) == 0:
    print("{0} 是偶数".format(num))
else:
    print("{0} 是奇数".format(num))
# 我们也可以使用内嵌 if 语句来实现：
# 执行以上代码输出结果为：
# 输入一个数字: 3
# 3是奇数



# 笔记
# 优化加入输入判断:
while True:
    try:
        num = int(input('输入一个整数：'))  # 判断输入是否为整数
    except ValueError:  # 不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')
    break




# 简洁就是美丽。
num = eval(input('Number:\n'))
print('{} is '.format(num) + ('even number.' if num % 2 == 0 else 'odd number.'))



# 取余操作非常慢，这里性能优化：

num = int(input("输入一个数字: "))
if (num & 1) == 0:
    print("{0} 是偶数".format(num))
else:
    print("{0} 是奇数".format(num))
