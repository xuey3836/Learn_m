
n = 3
l = [1,6,4]
import sys

i = 0
m = l[1]
while(i < n - 1):
    power_int = m
    for i in range(n):
        power_now = power_int * 2 - l[i]
        if (power_now < 0):
            m = m + 1
            break
        power_int = power_now
print(m)
    
