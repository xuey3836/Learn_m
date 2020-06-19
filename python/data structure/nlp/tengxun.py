n = 3
m = 5
ns = [1,2,3]
ms = [-1,-2,-4,-5,5]

ns.sort()
ms.sort()

s1 = ns[n-2]*ms[m-1]
s2 = ns[1]*ms[0]
s3 = ns[n-2]*ms[0]
s4 = ns[1]*ms[m-1]

print(max(s1,s2,s3,s4))


n =3
ns = [1, 5, 4]
p  = 0
for i in range(n-1):
    for j in range(i+1,n):
        x = ns[i]
        y = ns[j]
        if x*y ==0:
            p = p + 1
            continue
        elif x*y>0:
            if min(x,y) < abs(x-y):
                break
        else:
            if min(abs(x), abs(y)) < abs(x+y):
                break
        p = p + 1
print(p)





def shift(n, x):
    a = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    b =[]
    res =''
    while True:
        s = n//x
        y = n%x
        b = b+[y]
        if s==0:
            break
        n = s
    b.reverse()
    for i in b:
        res+= a[i]
    return res

if _name_ =="__main__":
    num = int(input())
    res = []
    for i in range(num):
        tmp = int(input())
        lis = list(map(str, input().split()))
        cal = str(int(lis[0], base=tmp))+lis[2]+str(int(lis[1], base = tmp))
        res.append(shift(eval(cal), tmp))





n =5 
m  = 4
name = []
name =['aaab','aab','aa','aabb','a']

res = []

start = 'a' 
stop = 'c'
select =[]
for i in range(len(name)):
    if name[i].startswith(start) and not name[i].endswith(stop):
        select.append(name[i])
select.sort()
res.append(select[0])
name.remove(select[0])

print(select[0])
