#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:53 
# @Author : huangting 
# @File : 016_range_prime_number.py
# 输出指定范围内的素数


# 素数（prime test_number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
# 以下实例可以输出指定范围内的素数：
#!/usr/bin/python3

# 输出指定范围内的素数

# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
# 执行以上程序，输出结果为：
# $ python3 test.py
# 输入区间最小值: 1
# 输入区间最大值: 100
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97




# 笔记
# 与前面判断是否是质数一样，作者算法中未使用到"开根号法"来节约时间复杂度，同时为加入个数等说明，因此我对其改进如下：
import math

# 输出指定范围内的素数
# 用户输入范围
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
print("素数结果如下：")
print("=" * 10)
pri_num = 0
com_num = 0
for num in range(lower, upper + 1):
    # 找到其平方根（ √ ），减少算法时间
    square_num = math.floor(num ** 0.5)
    # 素数大于 1
    if num > 1:
        for i in range(2, (square_num + 1)):
            if (num % i) == 0:
                com_num += 1
                break
        else:
            pri_num += 1
            print(num)
print("=" * 10)
print(com_num, '个合数')
print(pri_num, '个素数')




# 先定义一个判断素数的函数，然后再输入范围去判断。
# -*- coding: UTF-8 -*-

# Filename : defprime.py
# author ：Pt

def isprime(x):
    if x == 1:
        return False
    k = int(x ** 0.5)
    for j in range(2, k + 1):
        if x % j == 0:
            return False
    return True


lower = int(input("请输入区间最小值："))
upper = int(input("请输入区间最大值："))
for i in range(lower, upper):
    if isprime(i):
        print(i, end=" ")





prime_number = [x for x in range(int(input('区间最小值：')), int(input('区间最大值：'))) if
                [] == [y for y in range(2, int(x ** 0.5) + 1) if x % y == 0]]

print(prime_number)






# 在已经定于的数值中求所有的素数。
# 在x**y中求素数，千万别作死求太大的数，会没耐心等结果。
i = 2
x = input("请输入x的值:")
y = input("请输入y的值:")
x = int(x)
y = int(y)
s = x ** y
s = int(s)
while (i < s):
    j = 2
    while (j <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i / j):
        print(str(i) + ",")
    i = i + 1

# 这个是求梅森素数的:
def meisen(n):
    n += 1
    while True:
        k = n % 2
        n = n // 2
        if k != 0:
            return False
        if n == 1:
            break
    return True


def sushu():
    n = 1
    while True:
        if n == 1 or n == 2 or n == 3:
            yield n
        else:
            m = n // 2
            flag = False
            for i in range(2, m + 1):
                if n % i == 0:
                    flag = True
            if not flag:
                yield n
        n += 1


import time

begin_time = time.time()
for i in sushu():
    if i > 10000:  # 改 i >的值可以增加求取范围
        break
    if meisen(i):
        print(i)
        end_time = time.time()
        print(end_time - begin_time)
        begin_time = end_time







# 修正重复输出质数的错误:
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            elif i < (num - 1):
                continue
            else:
                print(num)





# 把版大的改造了下，增加平方根和只從質數判斷是否為質數，算大數字會快很多。
import math

# 創建列表儲存質數
listPM = [2]
lower = int(input("最小值: "))
upper = int(input("最大值: "))
# 質數從2開始
if upper >= 2:
    # 平方根減少運算
    for num in range(3, upper + 1):
        S_num = math.sqrt(num)
        # 只從質數判斷是否為質數
        for i in listPM:
            if i > S_num:
                listPM.append(num)
                break
            if (num % i) == 0:
                break
    # 剔除掉小於的質數
    listPM = [i for i in listPM if i >= lower]
    print(listPM)





# hizmz真大佬，不过代码我研究了很久，还是给大佬加上注释如下，并对负数进行改进，如果需要，还可以自行添加对其他字符串进行限定输入。
# 输出指定范围内的素数
# 非数字字符串会出错，一开始就应该避免错误的发生（限定范围），而不是报错了再来改进，
# 可以继续改进用列表输出质数和合数
import math

lower = int(input("输入区间(包括)最小值: "))
upper = int(input("输入区间(包括)最大值: "))
sumzs = 0
sumhs = 0
print("素数结果如下：")
print("=" * 10)

pri_num = 0
com_num = 0

for num in range(lower, upper + 1):
    if num > 1:  # 素数大于 1
        square_num = math.floor(num ** 0.5)  # 找到其平方根，减少算法时间
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for i in range(2, (square_num + 1)):  # （2,2）属于空集，不会出错，但也不会执行
            if (num % i) == 0:  # 可以被整除说明是合数
                com_num += 1
                sumhs += num
                print(num, "是合数")
                break  # 执行到这里说明是合数，跳出里层for和所有else语句，执行完其他语句（比如下面注释掉的）后继续外一层for的下一次循环
            else:  # 不能被依次整除，说明循环完了还是质数，用pass表示占位
                pass  # 继续执行下一句else语句
        # 这里的else和上面的for属于一个级的，能执行下面的语句说明上面的质数筛选已经过关了，没有执行break。
        else:  # 上面的for模块执行完了，说明都不能被2到平方根的数整除
            pri_num += 1  # 所以质数计数+1
            sumzs += num
            print(num, "是质数")
    #        print(num,"是质数")       #这就是break执行后继续执行的语句，同for和else级别，也就是上面说的其他语句
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    else:
        print(num, "既不是素数也不是合数")
print("=" * 10)
print(com_num, '个合数', '和为', sumhs)
print(pri_num, '个素数', '和为', sumzs)
