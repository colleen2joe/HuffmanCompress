#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/9/4/004 15:16
# @Author: Colleen
# @File  : HuffTree.py
from Node import *


class HuffTree(object):
    def __init__(self, char_weights):
        self.leaf_lists = [Node(char_weights[i], i) for i in range(len(char_weights))]

        '''
        如果列表里还有叶节点
        将列表内叶节点按照值排序
        将值最小的两个叶节点值的和存入new_node节点
        将列表中最小的叶节点作为new_node的左节点，次小的叶节点作为new_node的右节点，
        与此同时叶节点列表删除这两个最小的叶节点（pop）
        将new_node存入叶节点列表中
        执行完while循环后赫夫曼树构建完毕，此时列表中只有一个叶节点，也是树的根节点.
        通过Node类的left、right属性遍历该树
        申明bits列表存放编码
        
        '''

        while len(self.leaf_lists) != 1:
            self.leaf_lists.sort(key=lambda node: node.value, reverse=True)
            new_node = Node(value=(self.leaf_lists[-1].value + self.leaf_lists[-2].value))
            new_node.left = self.leaf_lists.pop(-1)
            new_node.right = self.leaf_lists.pop(-1)
            self.leaf_lists.append(new_node)
        self.root = self.leaf_lists[0]
        self.bits = [1] * 1024

        '''
        用递归的思想生成编码
        length是编码长度，初始设为0，往子树遍历一步，length就加一
        往左子树遍历，路径为0，bits中的length位为0
        往右子树遍历，路径为1，bits中的length位为1       
        '''

    def pre(self, tree, length, d):
        node = tree
        code = ''
        if (not node):
            return
        elif node.name:
            print(str(node.name) + '的编码为：')
            for i in range(length):
                code += str(self.bits[i])
            print(code)
            d[node.name] = code
            return
        self.bits[length] = 0
        self.pre(node.left, length + 1, d)
        self.bits[length] = 1
        self.pre(node.right, length + 1, d)

    '''
    生成哈夫曼编码
    从根节点开始遍历，前序遍历，先根节点，后左子树，后右子树
    length初始值为0，随着遍历增加数值
    '''

    def get_code(self):
        d = {}
        self.pre(self.root, 0, d)
        return d
