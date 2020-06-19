a = 2
b = [2,2]

ntotal = 1
for i in b:
    ntotal = ntotal *i
maxi = max(b)
total = 1
for i in range(1, maxi+1):
    c = 0
    for l1 in b:
        if l1 >= i:
            for l2 in b:
                if l2 != l1:
                    if l2 > i:
                        c = c + i
                    else:
                        c = c + l2
    total = total + i*c

mean = total/ntotal
