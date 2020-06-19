# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        list = [1, 1]
        while len(list) <= number:
            new = 0
            for i in range(len(list)):
                new = new + list[i]
            list.append(new)
        return list[number]

p = Solution()
p.jumpFloorII(3)