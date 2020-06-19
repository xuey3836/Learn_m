m = 3
n = 32
w = [2,5,3]
v = [2,1,3]

nr = n
sv = sum(v)
rest = 0
for k in range(min(w)+1, max(w)+1):
    nr = nr - sv
    for i in range(m):
        if k <= w[i]:
            nr = nr + v[i]
    if nr < 0:
        k = k - 1
        break
if (k == max(w) and nr > 0):
    rest =  int(nr/sv)
print(k + rest)

