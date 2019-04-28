#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (33.72%)
# Total Accepted:    307.1K
# Total Submissions: 725.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        len_nums = len(nums)
        result = nums[0] +  nums[1] + nums[2]
        for i in range(len_nums):
            if (i != 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = len_nums - 1
            while (j < k):
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target - s)
                if diff ==0:
                    return s
                else:
                    if diff < abs(target - result):
                        result = s
                    if s < target:
                        j = j + 1
                    else:
                        k = k - 1
        return result



# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums = sorted(nums)
#         len_nums = len(nums)
#         re = nums[0] + nums[1] + nums[2]
#         for i in range(len_nums):
#             if (i != 0 and nums[i] == nums[i-1]):
#                 continue
#             for j in range(i+1, len_nums-1, 1):
#                 if (j !=i+1  and nums[j] == nums[j-1]):
#                     continue
#                 s = target - nums[i] - nums[j]
#                 if s >= nums[len_nums -1]:
#                     numsk = nums[len_nums-1]
#                 elif s <= nums[j+1]:
#                     numsk = nums[j+1]
#                 else:
#                     p = j + 1
#                     q = len_nums - 1
#                     while(p < q):
#                         k = int((p+q)/2)
#                         if s > nums[k]:
#                             p = k
#                         elif s < nums[k]:
#                             q = k
#                         else:
#                             break
#                         numsk  = nums[k]
#                 if abs(s - numsk) <  abs(target - re):
#                     re = nums[i] + nums[j] + numsk
#         return re
        

