#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 16:36 
# @Author : huangting 
# @File : 011_is_number.py
# 判断字符串是否为数字


# 以下实例通过创建自定义函数is_number()方法来判断字符串是否为数字：

# author by : www.runoob.com

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False
# 我们也可以使用内嵌 if 语句来实现：
# 执行以上代码输出结果为：
# False
# True
# True
# True
# True
# True
# True
# True
# False

# 更多方法
# Python isdigit()方法检测字符串是否只由数字组成。
# Python isnumeric()方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。




# 笔记
# 教程代码当出现多个汉字数字时会报错，通过遍历字符串解决
# 对汉字表示的数字也可分辨
def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        for i in s:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
            # return True
        return True
    except (TypeError, ValueError):
        pass
    return False




# 进一步扩展到全角数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    import unicodedata
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    if len(s) < 2:
        return False

    try:
        d = 0
        if s.startswith('－'):
            s = s[1:]
        for c in s:
            if c == '－':  # 全角减号
                return False

            if c == '．':  # 全角点号
                if d > 0:
                    return False
                else:
                    d = 1
                    continue
            unicodedata.numeric(c)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print(f'{is_number("foo")}')
print(f'{is_number("1")}')
print(f'{is_number("1.3")}')
print(f'{is_number("-1.37")}')
print(f'{is_number("1e3")}')
print(f'{is_number("2.345.6")}')
print(f'{is_number("-5.2-8")}')
print(f'{is_number("52-8")}')
print(f'{is_number("-.5")}')
print(f'{is_number("-5.")}')
print(f'{is_number(".5")}')

# 测试Unicode
# 阿拉伯语 5
print(f'{is_number("٥")}')
# 泰语 2
print(f'{is_number("๒")}')
# 中文数字
print(f'{is_number("四")}')
print(f'{is_number("四卅")}')
# 全角数字
print(f'{is_number("１２３")}')
print(f'{is_number("-１２３")}')
print(f'{is_number("－１２３")}')
print(f'{is_number("１２－３")}')
print(f'{is_number("１２３－")}')
print(f'{is_number("１.２３")}')
print(f'{is_number("１．２３")}')
print(f'{is_number("．２３")}')
print(f'{is_number("－．２３")}')
print(f'{is_number("１．23")}')
print(f'{is_number("１．２．３")}')
# 版权号
print(f'{is_number("©")}')
