#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        while ind < len(nums) - 1:
            if nums[ind] == val:
                del nums[ind]
                ind -= 1
            ind += 1
        return len(nums)

