#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:48 
# @Author : huangting 
# @File : 015_prime_number.py
# 质数判断

# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。

# author by : www.runoob.com

# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")
# 执行以上代码输出结果为：
# $ python3 test.py
# 请输入一个数字: 1
# 1 不是质数
# $ python3 test.py
# 请输入一个数字: 4
# 4 不是质数
# 2 乘于 2 是 4
# $ python3 test.py
# 请输入一个数字: 5
# 5 是质数



# 笔记
# 原作者的算法基本正确，但时间复杂度较高，在判断一个大数是质数还是合数的情况下，应该在查看因子那里的循环中使用到平方根。代码如下：
# Python 程序用于检测用户输入的数字是质数还是合数
import math

# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    # 找到其平方根（ √ ），减少算法时间
    square_num = math.floor(num ** 0.5)
    # 查找其因子
    for i in range(2, (square_num + 1)):  # 将平凡根加1是为了能取到平方根那个值
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
        # 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "既不是质数，也不是合数")
# 原理是用了开根号法：
# 假如一个数N是合数,它有一个约数a,那么有a×b=N
# 则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N。
# 因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数。





# -*- coding: UTF-8 -*-

# 用while循环，进行质数判断
# 输入数字

num = int(input("输入一个数字："))
# 定义i
i = 2
while i < num:
    s = num % i
    if s == 0:
        print("{}能被除的数其中有{}".format(num, i))
        break
    else:
        i += 1
if num == i:
    print("是质数")
else:
    print("不是质数")




# 输出1 - 100以内的质数：
count = 0
for i in range(1, 101):
    for j in range(1, i):
        if j == i // 2 and i % j == 1 or (i <= 3 and i != 1):
            if count == 4:
                print(i)
                count = 0
            else:
                print(i, end='\t')
                count += 1
            break
        if i % j == 0 and j != 1:
            break




# 用质数表来判断是否为质数
# -*- coding: UTF-8 -*-
# Python 程序用于检测用户输入的数字是否为质数
# 用户输入数字
num = int(input("请输入一个数字: "))


# 获取小于等于num平方根的质数表
def getPrimeList(n, oldPrimeList):
    for prime in oldPrimeList:
        if (n % prime) == 0:
            break
    if prime == oldPrimeList[-1]:
        oldPrimeList.append(n)


# 2,3是质数
if num == 2 or num == 3:
    print(num, "是质数")
# 对大于3的数用质数表来判断
elif num > 3:
    judge_num = int(num ** 0.5) + 1
    primeList = [2]
    for i in range(2, judge_num):
        getPrimeList(i, primeList)
    for i in primeList:
        if (num % i) == 0:
            print(num, "不是质数")
            break
    else:
        print(num, "是质数")
# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")




# 参考方法：
# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, (int(num / 2) + 1)):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")




# 参考方法：
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 用户输入数字
num = int(input("请输入一个数字: "))
if is_prime(num):
    print(num, "是质数")
else:
    print(num, "不是质数")




# 加入整数判断：
while True:
    try:
        num = int(input('输入一个整数：'))  # 判断输入是否为整数
    except ValueError:  # 不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    break
if num <= 1:
    print(num, "小于1的不是质数")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
        elif i < (num - 1):
            continue
        else:
            print(num, "是质数")




# Python3计算质数 （厄拉多塞筛法）
# ls3[1:6:2] -- 起始位置为 2，终止位置为 6，步长为2
def countPrimes(self, n: int) -> int:
    if n < 3:
        return 0
    else:
        # 首先生成了一个全部为1的列表
        output = [1] * n
        # 因为0和1不是质数,所以列表的前两个位置赋值为0
        output[0], output[1] = 0, 0
        # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
        # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
        for i in range(2, int(n ** 0.5) + 1):
            if output[i] == 1:
                output[i * i:n:i] = [0] * len(output[i * i:n:i])
    # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
    return sum(output)




# 参考：
while 1:
    try:
        a = int(input('请输入一个需要判断是否是质数的数：'))
        if a <= 0:
            print('请输入一个正整数。')
        elif a == 1:
            print('1不是质数也不是合数。')
        elif a == 2:
            print('2是质数。')
        else:
            for i in range(2, a):
                if a % i == 0:
                    print('{0}是合数，{0}={1}×{2}。'.format(a, i, a // i))
                    break
            else:
                print('{0}是质数。'.format(a))
    except ValueError:
        print('请输入一个数。')





# 参考：
lower_range = int(input('Key in the lower range: '))
upper_range = int(input('Key in the upper range: '))

list_prime = []
num_prime = 0


# 定义一个函数来判断给定一个数n是否是质数，输入True（质数），False（合数）
def is_prime(n):
    decision = False

    for i in range(2, n):
        if n % i == 0:
            decision = False
            return decision
            break
        else:
            continue

    decision = True
    return decision


for i in range(lower_range, upper_range + 1):

    outcome = is_prime(i)

    if outcome == True:
        list_prime.append(i)
        num_prime += 1
    else:
        continue

print(list_prime)
print(num_prime)





# 企图结合平方根算法和厄拉多塞筛法一起用，但是代码会复杂很多，转念一想，如果遍历剔除倍数的操作 比 一个个判断整除的操作 ，并没有省去多长时间，那么可能就不如直接用平方根算法了吧。
# 赞同 hizmz 的代码原理，补充一下注释吧，大佬牛逼。
# 用平方根算法减少时间
import math

# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    # 因为向上向下取整的函数对于整数来说都是自身，所以要想查找因子必须+1来包括自身
    # 所以用的是向下取整函数，否则向上取整后比如平方根是5.2>>6>>7多算一个6
    pingfanggeng = math.floor(num ** 0.5)
    # 查找其因子
    for i in range(2, pingfanggeng + 1):  # 向下取整后需要加一来判断平方根位的因数，包括平方根
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
        # 如果输入的数字小于或等于 1，那就不是质数
else:
    print(num, "既不是质数，也不是合数")
