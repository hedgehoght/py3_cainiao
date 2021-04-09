#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/9 16:10 
# @Author : huangting 
# @File : usewget.py
# 学使用wget

import os

import requests
import wget
import tempfile

url = 'http://192.168.3.37/FileType.check1'

# # 获取文件名
# file_name = wget.filename_from_url(url)
# print(file_name)
#
# # 下载文件，使用默认文件名,结果返回文件名
# file_name = wget.download(url)
# print(file_name)
#
# # 下载文件，重新命名输出文件名
# target_name = 't1.jpg'
# file_name = wget.download(url, out=target_name)
# print(file_name)
#
# # 创建临时文件夹，下载到临时文件夹里
# tmpdir = tempfile.gettempdir()
# target_name = 't2.jpg'
# file_name = wget.download(url, out=os.path.join(tmpdir, target_name))
# print(file_name)


def urldownload(url,filename=None):
    """
    下载文件到指定目录
    :param url: 文件下载的url
    :param filename: 要存放的目录及文件名，例如：./test.xls
    :return:
    """
    down_res = requests.get(url)
    with open(filename,'wb') as file:
        file.write(down_res.content)



