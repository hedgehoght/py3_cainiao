#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:44 
# @Author : huangting 
# @File : 014_max.py
# 获取最大值函数


# 以下实例中我们使用max()方法求最大值：

# author by : www.runoob.com

# 最简单的
print(max(1, 2))
print(max('a', 'b'))

# 也可以对列表和元组使用
print(max([1, 2]))
print(max((1, 2)))

# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))
# 执行以上代码输出结果为：
# 2
# b
# 2
# 2
# 80, 100, 1000 最大值为: 1000
# -20, 100, 400 最大值为: 400
# -80, -20, -10 最大值为: -10
# 0, 100, -400 最大值为: 100





# 笔记
# 对比任意多个数字的大小
# 参考：
N = int(input('输入需要对比大小数字的个数：'))
print("请输入需要对比的数字：")
num = []
for i in range(1, N + 1):
    temp = int(input('输入第 %d 个数字' % i))
    num.append(temp)

print('您输入的数字为：', num)
print('最大值为：', max(num))




# 参考方法：
N = int(input('输入需要对比大小数字的个数：\n'))

num = [int(input('请输入第 %d 个对比数字 \n' % (i))) for i in range(1, N + 1)]

print('您输入的数字为:', list(num))
print('最大值为: ', max(num))




# 相比以上不用输入对比大小数字的个数:
a = []

while True:
    """输入q来结束输入数字"""
    try:
        a.append(int(input("输入数字: ")))
        break
    except ValueError:
        print("输入的不是数字")
while a[-1] != 'q':
    c = input("输入数字: ")
    if c != 'q':
        try:
            a.append(int(c))
        except ValueError:
            print("输入的不是数字")
    else:
        a.append(c)

del a[-1]

print("最大数字是", max(a))




# 感觉比楼上的稍微好理解一点：
# -*- coding UTF-8 -*-
# author by:Lebron
a = []
while True:
    # 输入q来结束输入数字
    c = input('请输入数字：')
    if c != 'q':
        try:
            i = int(c)
            a.append(i)
        except ValueError:
            print('输入的不是数字')
    else:
        break
print('最大数字是：', max(a))
