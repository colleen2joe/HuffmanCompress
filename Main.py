#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/4/004 15:28
# @Author: Colleen
# @File  : Main.py
from Compress import *
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please input the input file name !')
        sys.exit()

    input_file = sys.argv[1]
    output_file = input_file + '.zzz'  # 压缩后不要随意修改文件名(解压需要)
    compress(input_file, output_file)
