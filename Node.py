#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/4/004 15:13
# @Author: Colleen
# @File  : Node.py


class Node(object):
    def __init__(self, value, name=None):
        self.value = value
        self.name = name  # name表示一个字节表示的字符对应的十进制数
        self.left = None
        self.right = None
