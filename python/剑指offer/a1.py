n = 6 
line = "AaAaAA"
t1 = 0
t2 = 0
t3 = 1
pre  = "lower"
for i in range(n):
    a = line[i]
    if a.islower():
        t1 = t1 + 1
        t3 = t3 + 2
        if pre == "lower":
            t2 = t2 + 1
        else:
            t2 = t2 + 2
            pre = "lower"
    else:
        t1 = t1 + 2
        t3 = t3 + 1
        if pre == "lower":
            t2 = t2 + 2
            pre = "upper"
        else:
            t2 = t2 + 1
m = [t1, t2,t3]
print(min(m))

