#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 12:50 
# @Author : huangting 
# @File : change_file_name.py

# 将自己的一些歌名称修改

import os
import re

path = 'D:/娱乐/音乐/英文歌-'
i = 1
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
        file_name = os.path.basename(os.path.join(path, file))
#设置新文件名
        new_name = re.sub(r' \[.*\]', '', file_name )
        print(new_name)
#重命名
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
#结束
print ("End")
