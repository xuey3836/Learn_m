#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (25.84%)
# Total Accepted:    704.4K
# Total Submissions: 2.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len ==0:
            return 0
        elif s_len ==1:
            return  1
        maxsub = 1
        for i in range(s_len - 1):
            sub =  [s[i]]
            j = i + 1
            while j < s_len and s[j] not in sub :
                 sub.append(s[j])
                 j = j + 1
            if len(sub) > maxsub:
                maxsub = len(sub)
            if maxsub > len(s[i:]):
                break
        return maxsub



