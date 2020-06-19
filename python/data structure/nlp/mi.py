

 

m  = [-2, 11, -4, 13, -5, -2]
N = len(m)
ThisSum = MaxSum = 0; 
for i in range(N):
    ThisSum += m[i]
    if ThisSum>MaxSum:
        MaxSum = ThisSum
    elif ThisSum < 0:  
        ThisSum = 0 
print(ThisSum)



def maxProfit(prices):
    n=len(prices)
    if n==0:
        return 0
    left=[0]*n
    minmum, maxmum=prices[0], prices[0]
    profit=0
    for i in range(1,n):
        if prices[i]<minmum:
            minmum, maxmum=prices[i], prices[i]
        else:
            if maxmum<prices[i]:
                maxmum=prices[i]
        profit=max(profit, maxmum-minmum)
        left[i]=profit
    right=[0]*n
    minmum, maxmum=prices[n-1], prices[n-1]
    profit=0
    for i in range(n-2,-1,-1):
        if prices[i]>maxmum:
            minmum, maxmum=prices[i], prices[i]
        else:
            if prices[i]<minmum:
                minmum=prices[i]
        profit=max(profit, maxmum-minmum)
        right[i]=profit
    ans=0
    for i in range(n-1):
        ans=max(ans, left[i]+right[i+1])
    ans=max(ans, left[n-1], right[0])
    return ans
m = [2, 1, 5, 0, 2, 3, 1, 4]
print(maxProfit(m))          