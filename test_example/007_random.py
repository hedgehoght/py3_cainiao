#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:18 
# @Author : huangting 
# @File : 007_random.py
# 随机数生成


# 以下实例演示了如何生成一个随机数：

# author by : www.runoob.com

# 生成 0 ~ 9 之间的随机数

# 导入 random(随机数) 模块
import random

print(random.randint(0, 9))
# 执行以上代码输出结果为：
# 4

# 以上实例我们使用了random模块的randint()函数来生成随机数，你每次执行后都返回不同的数字（0到9），该函数的语法为：
# random.randint(a, b)
# 函数返回数字N ，N为a到b之间的数字（a <= N <= b），包含a和b。



# 笔记
# 一个简单的随机数字小游戏
# !/usr/bin/python
# -*- coding:utf-8 -*-

# 随机数字小游戏
import random

i = 1
a = random.randint(0, 100)
b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第%d输入的数字小于电脑随机数字' % i)
        b = int(input('请再次输入数字:'))
    else:
        print('你第%d输入的数字大于电脑随机数字' % i)
        b = int(input('请再次输入数字:'))
    i += 1
else:
    print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' % (i, b))





"""源自鱼C论坛用户的猜数字游戏"""

import random
import re
from sys import exit


def main():
    time = 3
    count = 1
    num = 0
    dict = {'0': 5, '1': 10, '2': 20, '3': 50, '4': 100}

    print('猜数字')
    go = int(input('开始：1\n结束：0\n->'))

    while go != 1 and go != 0:
        print('Input 1 or 0.')
        go = int(input('开始：1\n结束：0\n->'))  # 重复输入
    if go == 1:
        pass
    elif go == 0:
        exit()

    print('｛LV0.新手}｛LV1.简单｝｛LV2.一般｝｛LV3.困难｝｛LV4.噩梦｝｛LV5.地狱｝')
    r = input('Level:')
    r = re.sub('\D', '', r)  # 抽出数字

    if r.strip() == '':  # 检查是否含有数字
        print('隐藏难度｛LV6.调戏｝')
        n = 1000
        time = 99
    else:
        n = dict.get(r, 500)

    secret = random.randint(1, n + 1)  # 随机的范围 根据难度调整
    print('猜猜{1-%s}之间的数:' % n)

    while True:  # 机会内循环即可，猜中了可以用break跳出循环
        print('一定是：', end='')
        num = input()

        if num.isdigit():  # 检查玩家输入是否有误，防止程序崩溃
            num = int(num)
            if num < 1:
                print('现在就放弃太可惜了')
            elif num > n:
                print('超出范围')
            elif num > secret:
                print('太大')
            elif num < secret:
                print('太小')
            else:
                if count == 1:  # 算是奖励机制？
                    print('棒')
                elif count == 2:
                    print('赞')
                else:
                    print('好')
                break

            time -= 1
            count += 1  # 奖励机制计数

            if time == 0:
                print('正确答案：%s' % secret)
                break
            else:
                print('还有[%s]次机会:' % time)
        else:
            print('要崩溃了!!!')
    print('游戏结束!')


if __name__ == '__main__':
    main()





# 该程序会在字符终端1~24之间的位置随机打印出一个星号 * ，并提示“请输入一个移动星号的指令(L / l or R / r)):”，如果用户输入L并回车，星号就会向左移动一个字符的位置，并被重新输出；如果用户输入R并回车，星号则会向右移动一个字符的位置，程序会循环提示用户输入，直至用户输入 “EXIT”，程序退出。
import random


class computer(object):

    def __init__(self):
        pass

    g_num = 0

    def ger_num(start, end):
        return random.randint(start, end)

    def contrl(ctl_str):
        global g_num
        if ctl_str == 'l' or ctl_str == 'L':
            g_num -= 1
            if g_num < 0:
                g_num = 23
        elif ctl_str == 'r' or ctl_str == 'R':
            g_num += 1
            if g_num > 23:
                g_num = 0
        return g_num

    @staticmethod
    def print_space(space_num):
        print_content = ['-'] * 24
        print_content = ''.join(print_content)
        l_content = list(print_content)
        l_content[space_num] = '*'
        l_content = ''.join(l_content)
        print(l_content)


if __name__ == '__main__':
    # 生成随机数，确定星号的位置
    g_num = computer.ger_num(0, 24)
    computer.print_space(g_num)
    while True:
        ctrl_str = input("请输入移动星星的指令(L/l or R/r):")
        if ctrl_str == 'EXIT' or ctrl_str == 'exit':
            break
        g_num = computer.contrl(ctrl_str)
        computer.print_space(g_num)




# 产生一个1到10的随机整数:
random.randint(1, 10)
# 产生一个0到1的随机浮点数:
random.random()
# 产生一个1.1到5.4之间的随机浮点数:
random.uniform(1.1, 5.4)
# 从序列中随机选取一个元素:
random.choice(' ')
# 生成从1到100间隔为2的随机整数:
random.randrange(1, 100, 2)
