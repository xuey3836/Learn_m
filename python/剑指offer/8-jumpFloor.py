# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        list = [1, 1]
        while len(list) <= number:
            list.append(list[-1]+ list[-2])
        return list[number]
        
p = Solution()
p.jumpFloor(5)