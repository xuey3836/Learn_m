#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (44.89%)
# Total Accepted:    474.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)

        while l1 or l2:
            if not l1:
                n.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                n.next = ListNode(l1.val)
                l1 = l1.next
            else:                
                v1 = l1.val
                v2 = l2.val
                if v1 < v2:
                    n.next = ListNode(v1)
                    l1 = l1.next
                else:
                    n.next = ListNode(v2)
                    l2 = l2.next
            n = n.next
 
        return root.next
        
