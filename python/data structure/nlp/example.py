t = 'a'

i = 0
a = t[i]
n = len(t)
p  = 0
re = []
while i < n:
    s = t[i]
    if a == s:

        p = p + 1

    else:c
        re.append(str(p))
        re.append(a)
        a = s
        p = 1
    i = i + 1
    if i == n:
        re.append(str(p))
        re.append(a)
print(str(re))

