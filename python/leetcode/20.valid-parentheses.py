#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.46%)
# Total Accepted:    477.4K
# Total Submissions: 1.3M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set = {"(":")", "[":"]", "{":"}"}
        values = set.values()
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        while s != "":
            if s[0] in values:
                return False
            for i, letter in enumerate(s):
                if letter in values:
                    if letter != set[s[i-1]]:
                        return False
                    else:
                        s = s[:(i-1)] + s[i+1:]
                        break
        return True
# s = "()"
# t = Solution()
# t.isValid(s)

# s = "{}{{]]"
# t.isValid(s)
