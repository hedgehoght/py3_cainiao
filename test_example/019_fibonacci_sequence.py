#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 17:05 
# @Author : huangting 
# @File : 019_fibonacci_sequence.py
# 斐波那契数列

while True:
    try:
        n1 = 0
        n2 = 1
        count = 2
        num = int(input('输入整数：'))
        if num < 1:
            print('请输入大于1的数')
        elif num == 1:
            print('数列为：')
            print('{0}'.format(n1))
        else:
            print('数列为：')
            print(n1, n2, end=' ')
            while count < num:
                ni = n1 + n2
                print(ni, end=' ')
                n1 = n2
                n2 = ni
                count += 1
    except ValueError:
        print("输入错误，请重新输入")



# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
# Python 实现斐波那契数列代码如下：

# author by : www.runoob.com

# Python 斐波那契数列实现

# 获取用户输入数据
nterms = int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
# 执行以上代码输出结果为：
# 你需要几项？ 10
# 斐波那契数列：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,



# 笔记
# 参考方法：
num = int(input("输入一个整数："))
f1 = 0
f2 = 1
if num <= 0:
    print("请输入一个正整数！")
elif num == 1:
    print("斐波拉契数列：%d" % f1)
else:
    print("斐波拉契数列：", end="")
    print(f1, f2, end=" ")
    for n in range(1, num - 1):
        f = f1 + f2
        f1, f2 = f2, f
        print(f, end=" ")




# 参考方法：
L = [0, 1]
num = int(input("请输入你要的项数："))
if (num <= 0):
    print("请输入一个正整数！");
elif (num <= 2):
    if (num == 1):
        print("数列是：0")
    else:
        print("数列是：0,1")
else:
    for i in range(2, num):
        f = L[i - 1] + L[i - 2]
        L.append(f)
    print("数组是：")
    print(L)




# 抛砖引玉一下：
def fab(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fab(n - 1) + fab(n - 2)


def printfablist(n):
    for i in range(1, n + 1):
        print(fab(i), end=' ')


# 运行实例：
# >>>printfablist(int(input('please input a test_number:')))
# please input a test_number:10
# 0 1 1 2 3 5 8 13 21 34




# 两种实现方式，第一种是通过循环实现，第二种是通过递归调用来实现。第二种代码稍显简洁，结构较清晰，但由于递归占用较多资源，对于大规模的计算消耗比较大，运算比较慢。反而通过循环实现的运算较快。代码如下
num = int(input("请输入要输出多少项："))
print("-------递归-------");


def Count_Function(n):
    if (n < 3):
        return (n)
    else:
        return (Count_Function(n - 1) + Count_Function(n - 2))


i = 1
while (i <= num):
    print(Count_Function(i), end="\t")
    i += 1
print()

# 计算斐波那契数列，通过循环来实现
num = int(input("请输入您要显示的项数："))
print("-------循环-------");
n = 3
a = [1, 2]
if (num == 1):
    print(a[0], end=" ")
elif (num == 2):
    print(a[num - 2], a[num - 1], end=" ")
else:
    while (n <= num):
        temp = a[n - 2] + a[n - 3]
        a.append(temp)
        n += 1
    for i in a:
        print(i, end=' ')
print()




# 参考方法：
# -*- coding: UTF-8 -*-

while True:
    try:
        count = int(input("请输入所需斐波那契数列的数量："))
        if count < 1:
            print("请输入一个大于0的数字：")
        elif count == 1:
            print("[0]")
        # count>=2的情况
        else:
            i, j = 0, 1  # 初始化i,j，表示相邻的两个数
            f_list = [0, 1]  # count==2时，斐波那契数列
            while count > 2:
                i, j = j, i  # 交换i,j的值，上一次计算的j变成下一次计算的i
                j += i  # 计算i和j后面一个数的值并且赋给j
                f_list.append(j)  # 将j追加给列表
                count -= 1
            print(f_list)
    except ValueError:
        print("输入错误，请重新输入")




# 参考方法：
n = int(input('输入斐波那契数列的目标数字：'))


def fibo2(n):
    a, b = 0, 1
    arr = [0, 1]
    while 1:
        if a + b <= n:
            arr.append(a + b)
            a, b = b, a + b
        else:
            break
    return arr


print(fibo2(10))




# 简洁版斐波那契数列：
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(1000)  # 取值范围可以任意

# 输出结果如下：
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987




# 参考：
# 斐波那契数列的通项式为:f(n) = (5**0.5/5)*(((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n)

N = int(input("请输入要几项:"))
if (N < 0):
    print("请输入大于0的数")
else:
    for i in range(0, N):
        print(int((5 ** 0.5 / 5) * (((1 + 5 ** 0.5) / 2) ** i - ((1 - 5 ** 0.5) / 2) ** i)))
