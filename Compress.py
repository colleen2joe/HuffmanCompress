#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/5/005 14:21
# @Author: Colleen
# @File  : Compress.py
from HuffTree import *
from Constant import *


def count_weight(fin):
    """
    统计词频
    源文件需保存为ascii码格式
    :param fin: 文件对象
    :return:字符列表，长度为字符的种数，第length个数值表示第length个字符的词频
    """
    weights = [0 for i in range(CHAR_NUM)]
    c = fin.read(1)  # 读取一个字节
    while c:
        weights[int.from_bytes(c, 'little')] += 1  # 把bytes类型的变量x，转化为十进制整数
        c = fin.read(1)
    return weights


def encoding_file(fin, fout, map_dic):
    """
    编码文件
    :param fin: 输入文件
    :param fout: 输出文件
    :param map_dic: 字符到编码的映射字典
    :return: 编码总长度，当前待输出的比特数
    """
    total = 0  # 编码总长度，字节为单位
    size = 0  # 当前待输出的比特数
    cur = 0  # 待输出的一个字节的编码串

    c = fin.read(1)
    while c:
        if int.from_bytes(c, 'little') in map_dic:
            code = map_dic[int.from_bytes(c, 'little')]  # 根据一个字节c的十进制表达找到字典中对应的编码
        else:
            print('not exit')
        for i in range(len(code)):
            if code[i] == '0':
                cur = cur << 1  # 左移一位
            else:
                cur = (cur << 1) | 1  # 左移一位再和1位或
            size += 1
            if size == BYTE_SIZE:
                fout.write(cur.to_bytes(1, 'little'))  # 把cur转为二进制编码串，长度为1字节
                total += 1
                size = 0
                cur = 0
        c = fin.read(1)

    if size:
        # 不足一个字节
        # 低位补0
        cur = cur << (BYTE_SIZE - size)
        fout.write(cur.to_bytes(1, 'little'))  # 把cur转为二进制编码串，长度为1字节
        total += 1
    else:
        size = 8

    return total, size


def compress(fin_name, fout_name):
    """
    压缩文件
    :param fin_name: 输入文件名
    :param fout_name: 输出文件名
    :return:null
    """
    fin = open(fin_name, 'rb')
    fout = open(fout_name, 'wb')

    weights = count_weight(fin)

    hufftree = HuffTree(weights)
    d = hufftree.get_code()
    print(d)

    """
    重新读取文件
    编码后输出到输出文件
    """
    fin.seek(0)
    total, num = encoding_file(fin, fout, d)
    print('total=%s, num=%s' % (total, num))  # debug

    # 在输出文件内保存字符频数表
    for i in range(CHAR_NUM):
        fout.write(weights[i].to_bytes(FOUR, 'little'))

    # 保存total, num
    fout.write(total.to_bytes(FOUR, 'little'))
    fout.write(num.to_bytes(FOUR, 'little'))

    fout.close()
    fin.close()

    src_file_size = hufftree.root.value  # 源文件大小
    dst_file_size = total + CHAR_NUM * FOUR + FOUR * 2  # 目标文件大小

    print('%s compress as %s' % (fin_name, fout_name))
    print('dst/src = %s/%s ~= %s' % (dst_file_size, src_file_size, dst_file_size / src_file_size))
