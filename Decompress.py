#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/6/006 14:59
# @Author: Colleen
# @File  : Decompress.py
import sys
from Constant import *
from HuffTree import *


def read_weights(fin):
    """
    读取词频表
    :param fin: 文件对象
    :return: 词频表
    """
    weights = [int.from_bytes(fin.read(FOUR), 'little') for i in range(CHAR_NUM)]
    return weights


def decoding(fin, fout, root, total, num):
    """
    解码文件
    :param fin: 输入文件
    :param fout: 输出文件
    :param root: 根节点
    :param total: 总字节数
    :param num: 最后一个字节的有效位数
    :return:
    """
    cur = root
    for byte in range(total):
        code = int.from_bytes(fin.read(1), 'little')
        n = num if byte == total - 1 else BYTE_SIZE
        for bit in range(n):
            if code & MASKS[bit]:  # 按位与操作，若结果大于0说明该位为1
                cur = cur.right
            else:
                cur = cur.left
            if not (cur.right or cur.left):  # 左右子树都为空，达到叶节点
                name = cur.name
                fout.write(name.to_bytes(1, 'little'))  # 写入name的二进制表达
                cur = root


def decompress(input_name, output_name):
    """
    解压文件
    :param input_name: 输入文件名
    :param output_name: 输出文件名
    :return:
    """
    fin = open(input_name, 'rb')
    fout = open(output_name, 'wb')

    fin.seek(-(FOUR * 2), 2)  # seek(读取字符数，从哪里开始读)，2表示末尾，0表示开头，1表示当前位置
    total = int.from_bytes(fin.read(FOUR), 'little')
    num = int.from_bytes(fin.read(FOUR), 'little')

    # 读取字符的频率列表
    fin.seek(total, 0)
    weights = read_weights(fin)

    # 构建哈夫曼树
    hufftree = HuffTree(weights)
    d = hufftree.get_code()
    print(d)

    # 解码后输出到输出文件
    fin.seek(0, 0)
    decoding(fin, fout, hufftree.root, total, num)

    fin.close()
    fout.close()

    fin.close()
    fout.close()

    print('%s decompress as %s' % (input_name, output_name))
