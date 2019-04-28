#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.92%)
# Total Accepted:    565K
# Total Submissions: 2.3M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strvalue = str(x)
        if (strvalue[0] == "-"):
            ind = "-"
            strvalue = strvalue[1:]
        else:
            ind = ""
        result = ""
        for i in strvalue:
                result =  i + result 
        result = ind + result
        if (result[-1] == 0):
            result = result[:-1]
        rev = int(result)
        if (rev > 2**31-1 or rev < -2**31):
            return 0
        else:
            return(int(result))

        
