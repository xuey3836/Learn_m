#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         ind = 1
#         while ind < len(nums):
#             if nums[ind] == nums[ind-1]:
#                 del nums[ind]
#                 ind -= 1
#             ind += 1
#         return len(nums)


class Solution:
    def removeDuplicates(self, nums):
        c=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[c]=nums[i]
                c+=1
        return c
