#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:41 
# @Author : huangting 
# @File : 013_leap_year.py
# 判断闰年
# !/usr/bin/python3
# -*- coding: UTF-8 -*-

while True:
    try:
        year = int(input('输入一个整数：'))  # 判断输入是否为整数
    except ValueError:  # 不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if (year % 4) != 0:
        print('{0} is not 闰年'.format(year))
    elif (year % 100) != 0:
        print('{0} is  闰年'.format(year))
    elif (year % 400) != 0:
        print('{0} is not 闰年'.format(year))
    else:
        print('{0} is 闰年'.format(year))
    break




# 以下实例用于判断用户输入的年份是否为闰年：

# author by : www.runoob.com

year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))
# 我们也可以使用内嵌 if 语句来实现：
# 执行以上代码输出结果为：
# 输入一个年份: 2000
# 2000是闰年
# 输入一个年份: 2011
# 2011不是闰年


# 笔记
# 参考方法：
# !/usr/bin/python3

year = int(input("请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))




# 但其实Python的calendar库中已经封装好了一个方法isleap()来实现这个判断是否为闰年：
# >>> import calendar
# >>> print(calendar.isleap(2000))
# True
# >>> print(calendar.isleap(1900))
# False
# 根据用户输入判断：
import calendar

year = int(input("请输入年份："))
check_year = calendar.isleap(year)
if check_year == True:
    print("闰年")
else:
    print("平年")



# 参考：
# 简洁的代码最漂亮

year = int(input("请输入年份："))

print('闰年' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else '平年')
