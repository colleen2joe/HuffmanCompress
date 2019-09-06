#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/4/004 15:28
# @Author: Colleen
# @File  : Main.py
from Compress import *
from Decompress import *
import sys


def usage(name):
    '''打印帮助信息， 然后退出程序'''
    print('usage: python %s -c/-d file' % name)
    print('     -c compress')
    print('     -d decompress')
    sys.exit()


def main():
    if len(sys.argv) != 3:
        usage(sys.argv[0])

    opt, input_file = sys.argv[1:]

    if opt == '-c':
        # 压缩文件
        output_file = input_file + '.z'
        compress(input_file, output_file)
    elif opt == '-d':
        # 解压缩文件
        output_file = input_file.rsplit('.', 1)[0]  # 取'.z'之前的字符串作为输出文件的名字
        decompress(input_file, output_file)
    else:
        usage()


if __name__ == '__main__':
    main()
