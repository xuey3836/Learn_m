#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (75.74%)
# Total Accepted:    64.4K
# Total Submissions: 85K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        dict = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g",\
         "H":"h", "I":"i", "J":"j", "K":"k","L":"l", "M":"m", "N":"n", "O":"o",\
          "P":"p", "Q":"q", "R":"r", "S":"s", "T":"t", "U":"u", "V":"v", "W":"w", \
          "X":"x", "Y":"y","Z":"z"}
        keys = dict.keys()
        for s in keys:
            str = str.replace(s,dict[s])
        return str
            
