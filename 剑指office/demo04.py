"""
    时间限制：C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：860515
    本题知识点： 树
    题目描述
        输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
1. 分析

根据中序遍历和前序遍历可以确定二叉树，具体过程为：

    根据前序序列第一个结点确定根结点
    根据根结点在中序序列中的位置分割出左右两个子序列
    对左子树和右子树分别递归使用同样的方法继续分解 

例如：
前序序列{1,2,4,7,3,5,6,8} = pre
中序序列{4,7,2,1,5,3,8,6} = in

    根据当前前序序列的第一个结点确定根结点，为 1
    找到 1 在中序遍历序列中的位置，为 in[3]
    切割左右子树，则 in[3] 前面的为左子树， in[3] 后面的为右子树
    则切割后的左子树前序序列为：{2,4,7}，切割后的左子树中序序列为：{4,7,2}；切割后的右子树前序序列为：{3,5,6,8}，切割后的右子树中序序列为：{5,3,8,6}
    对子树分别使用同样的方法分解 
'''
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code hereif len(pre) == 0:
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:] )
        return root
        
        