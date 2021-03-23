#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 17:09 
# @Author : huangting 
# @File : 020_armstrong_number.py
# 阿姆斯特朗数

num = int(input("请输入要数字:"))
sum = 0
n = len(str(num))
temp = num
while temp > 10:
    i = temp % 10
    sum += i ** n
    temp = temp // 10
sum += temp ** n
if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")



lower = int(input("最小值: "))
upper = int(input("最大值: "))
for num in range(lower, upper + 1):
    sum = 0
    n = len(str(num))
    temp = num
    while temp > 0:
        i = temp % 10
        sum += i ** n
        temp = temp // 10
    if num == sum:
        print(num)





# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
# author by : www.runoob.com

# Python 检测用户输入的数字是否为阿姆斯特朗数

# 获取用户输入的数字
num = int(input("请输入一个数字: "))

# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))

# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# 输出结果
if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")
# 执行以上代码输出结果为：
# $ python3 test.py
# 请输入一个数字: 345
# 345 不是阿姆斯特朗数
#
# $ python3 test.py
# 请输入一个数字: 153
# 153 是阿姆斯特朗数
#
# $ python3 test.py
# 请输入一个数字: 1634
# 1634 是阿姆斯特朗数


# 获取指定期间内的阿姆斯特朗数

# author by : www.runoob.com

# 获取用户输入数字
lower = int(input("最小值: "))
upper = int(input("最大值: "))

for num in range(lower, upper + 1):
    # 初始化 sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)
# 执行以上代码输出结果为：
# 最小值: 1
# 最大值: 10000
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474

# 以上实例中我们输出了 1 到 10000 之间的阿姆斯特朗数。





# 笔记
# 参考方法：
# 获取小于指定数字的阿姆斯特朗数
num = int(input("pleace input a test_number: "))
sum = 0
i = 0
arr = [0, 0, 0, 0, 0]
print(num)
for k in range(1, num):
    n = len(str(k))
    m = n;
    # print(m,"->",k,"\n");
    i = 0;
    sum = 0
    while m > 0:
        m -= 1
        arr[i] = int(k / 10 ** m) % 10
        sum += arr[i] ** n
        i += 1
    if k == sum:
        print(k, end=",")




# 参考方法：
# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数
import math

x = int(input('请输入一个正整数:'))
x1 = x
n = len(str(x))
p = 0
for i in range(1, n + 1):
    y = math.floor(x // pow(10, n - i))
    print(y, end=',')
    m = pow(y, n)  # 也可以表达为:   m=y**n
    p = m + p
    x = x % pow(10, n - i)
print(p)
if p == x1:
    print('输入的数字 %d 是一个阿姆斯特朗数' % x1)
elif p != x1:
    print('输入的数字 %d 不是一个阿姆斯特朗数' % x1)




# 获取指定期间内的阿姆斯特朗数
lower = int(input("Please input a test_number: "))
upper = int(input("Please input a test_number: "))
sum = 0
for num in range(lower, upper):
    l = len(str(num))
    for n in str(num):
        sum = sum + int(n) ** l
    if num == sum:
        print(num)
    sum = 0




# 参考方法：
# 计算阿姆斯特朗数

count = 0
number = int(input('请输入一个正整数:'))  # 输入值并强制类型转换
lenth = len(str(number))  # 获取输入数字位数
list_number = list(str(number))  # 将数字转化为列表
for i in list_number:  # 将列表中的每一个元素以该元素的lenth次幂累加至count
    i = int(i)
    i = i ** lenth
    count = count + i

if count == number:  # 判断count与输入的数字是否相等，若相等则为阿姆斯特朗数
    print('是阿姆斯特朗数')
else:
    print('不是阿姆斯特朗数')



# 使用 lambda 表达式：
def is_armstrong(n):
    s = sum(map(lambda x: eval(x) ** len(str(n)), str(n)))
    return s == n


B = []
for i in range(1000):
    if is_armstrong(i):
        B.append(i)

print(B)
# 输出：
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

# 使用 list 的映射解析来进一步简化代码：
def is_armstrong(n):
    return n == sum([eval(i) ** len(str(n)) for i in str(n)])


B = [i for i in range(100000) if is_armstrong(i)]
print(B)
# 输出：
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084]




# 检查输入是否合法:
while (True):
    try:
        lower = int(input("最小值: "))
        upper = int(input("最大值: "))
    except ValueError:
        print("非法输入")
        continue
    if lower > upper:
        print("请检查输入大小")
        continue
    for num in range(lower, upper + 1):
        sum = 0
        n = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if num == sum:
            print(num)
    break




# 参考：
# 输出指定区间内的所有阿姆斯特朗数
try:
    lower = int(input("最小值："))
    upper = int(input("最大值："))
except ValueError:
    print("所输入内容非整数!")
    exit(1)

for num in range(lower, upper + 1):
    sum = 0
    n = len(str(num))

    for i in str(num):
        sum += int(i) ** n

    if sum == num:
        print(num)




# 一个推导式搞定一个3位数的算法
y = [(x // 100) ** 3 + ((x // 10) % 10) ** 3 + (x % 10) ** 3 for x in range(100, 1000) if
     (x // 100) ** 3 + ((x // 10) % 10) ** 3 + (x % 10) ** 3 == x]

print(y)

# [153, 370, 371, 407]
