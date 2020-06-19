n = 4 
h = [2, 1, 3, 2]
i = 0
t = 0
while len(h) > 0:
    t = t + 1
    mini = h.index(min(h))
    maxi = max(h[:mini])
    i = mini
    while h[i] < maxi:
        i = i + 1
        if i > len(h)-1:
            break
    h = h[i:]
print(t)

    
            
