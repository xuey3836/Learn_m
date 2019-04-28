#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.34%)
# Total Accepted:    220.9K
# Total Submissions: 735.3K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        l = len(nums)
        re = []
        for t in range(l):
            if (t != 0 and nums[t] == nums[t-1]):
                continue
            for i in range(t+1, l, 1):
                if (i != t+1 and nums[i] == nums[i-1]):
                    continue
                k = l - 1
                j = i + 1
                while (j < k):
                    s3 = nums[t] + nums[i] + nums[j] + nums[k] 
                    if (s3 == target):
                        re.append([nums[t],nums[i],nums[j],nums[k]])
                        j = j + 1
                #  Never let j refer to the same value twice (in an output) to avoid duplicates
                        while j < l and nums[j] == nums[j-1]:
                            j = j +1
                    elif(s3 > target):
                        k = k - 1
                    else:
                        j = j + 1
        return re  

