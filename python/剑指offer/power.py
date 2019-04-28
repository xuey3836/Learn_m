import sys
tasks = sys.stdin.readline().strip()
taskss = sorted(tasks)
res = taskss[2] - taskss[0]
print(res)


###
def down(m, n):
    l = m*n
    if (l == 1):
        return(1)
    if (m <=2 or n <=2):
        return(0)
    if (m ==1 or n ==1):
        return(l-1) 
    return((m-1)*(n-1))


import sys
a = input()

x = 1
def change(a):
    x += 1
    print(x)
change(x)

a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1
print (a)

import pandas as pd 
pd.read_csv()


def a(s):
    def b(t):
        return(s*t)
    

class Person:
    def __init__(self):
        pass
    def getAge(self):
        print(__name__)
p = Person()
p.getAge()
