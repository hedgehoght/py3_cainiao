#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/26 14:34 
# @Author : huangting 
# @File : log_sql.py

# 处理BDS 5.0的/var/www/html/php/runtime/common/log/20210326_sql.log日志，提取出sql语句
import re

file_name = 'C:/Users/zhangxuliang/Downloads/文件删除/log_sql_data.txt'

fo = open(file_name, 'rb')
print("文件名是：",fo.name)

for line in fo.readlines():  # 依次读取每行
    print("pass")
    if ( "SELECT" in line ) :
        print(line)

# 关闭文件
fo.close()




# for line in open(file_name):
#     print(line)

