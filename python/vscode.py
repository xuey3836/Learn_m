class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for t1 in range(l):
            complement = target - nums[t1]
            for t2 in range(t1,l):
                if complement == nums[t2]:
                    return [t1,t2]  

target = 8
nums = [2,3,6,10]
t = Solution()
t.twoSum( nums = nums, target = target)
