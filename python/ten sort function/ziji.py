
import pandas as pd
import numpy as np
import math

# n = 4
# m = [[0,3,1,5,8],
#     [3,0,6,7,9],
#     [1,6,0,4,2],
#     [5,7,4,0,3],
#     [8,9,2,3,0]]
# n =  4
m = [[0, 2,6, 5],
[2, 0, 4, 4],
[6, 4, 0, 2],
[5, 4, 2, 0]]

import sys


def TSP(s,init,num):
    if dp[s][init] !=-1 :
        return dp[s][init]
    if s==(1<<(n)):
        return m[0][init]
    sumpath=1000000000
    for i in range(n):
        if s&(1<<i):
            m1=TSP(s&(~(1<<i)),i,num+1)+m[i][init]
            if m1<sumpath:
                sumpath=m1
                path[s][init]=i
    dp[s][init]=sumpath
    return dp[s][init]

if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    m = []
    for i in range(n):   
        b = sys.stdin.readline().strip().split(',')
        b = map(int, b)
        m.append(b) 


    init_point=0
    path = [0]*2**(n+1)
    for i in range(len(path)):
        path[i] = [0]*n
    dp = [0]*2**(n+1)
    for i in range(len(path)):
        dp[i] = [-1]*n
    s=0
    for i in range(1,n+1):
        s=s|(1<<i)
    print(TSP(s,init_point,0))



 