# -*- coding:utf-8 -*-
class Solution:
    # def Fibonacci(self, n): 
    #     if n == 0:
    #         return 0
    #     if n == 1:           
    #         return 1
    #     else:            
    #         return self.Fibonacci(n-1) + self.Fibonacci(n-2)
    def Fibonacci(self, n):
        list = [0,1]
        while len(list) <= n:
            list.append(list[-1] + list[-2])
        return list[n]


p = Solution()
p.Fibonacci(5)