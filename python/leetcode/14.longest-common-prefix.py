#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.64%)
# Total Accepted:    379.9K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ""
        elif strs_len == 1:
            return strs[0]
        minstr  = strs[0]
        for str in strs:
            if (len(str) < len(minstr)):
                minstr = str
        l = len(minstr)
        common = ""
        for j in range(l):
            k = 0
            p = 1
            for str in strs:
                if minstr[0:(j+1)] not in str[0:(j+1)]:
                    p = 0
                    break
                else:
                    k = k + 1
            if p == 0:
                break
            if k == strs_len:
                if len(minstr[0:(j+1)]) > len(common):
                    common = minstr[0:(j+1)]
        return common
                    


        
