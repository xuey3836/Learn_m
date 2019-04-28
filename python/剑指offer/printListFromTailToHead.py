# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # if not isinstance(listNode, ListNode):
        #     return []
        res = []
        while listNode:
            # print(1)
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res

listNode = ListNode(67)
listNode.next = ListNode(0)
listNode.next = ListNode(24)   
listNode.next = ListNode(58)     