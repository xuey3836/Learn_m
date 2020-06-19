# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) ==0  or len(tin) == 0:
            return None

        root = TreeNode(pre[0])
        tinindex = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:(tinindex+1)], tin[:tinindex])
        root.right = self.reConstructBinaryTree(pre[(tinindex+1):], tin[(tinindex+1):])
        return root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
p = Solution()
p.reConstructBinaryTree(pre, tin)
        
        
        