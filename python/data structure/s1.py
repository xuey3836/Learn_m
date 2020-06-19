n = 7
k= 3
slen = [7,3, 1, 2, 6, 1, 1, 7, 1]

index = 0
mins = 0
for i in range(k):
    mins = mins + slen[i]

t = mins
for i in range(1,(n-k)):
    t = t - slen[i-1] + slen[i+k-1]
    if t < mins:
        mins = t
        index = i
print(index)