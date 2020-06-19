import sys
m,n,c = map(lambda x: int(x), sys.stdin.readline().split())
mat = [[0]*c for i in range(n)]
for i in range(n):
    line = [map(lambda x: int(x), sys.stdin.readline().split())]
    for j in range(line[0]):
        mat[i][line[j+1]-1] = 1
nc = 0
for j in range(c):
    k = 0
    b = []
    for i in range(n):
        if a[i][j] == 1:
            k = k + 1
            b.append(i)
    if (k > 1):
        for s in range(k-1):
            if b[s+1] - b[s] < m:
                nc = nc + 1
                break
print(nc)