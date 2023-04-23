value = map(int,input())
s = [0,0]
pre = value[0]
for v in value[1:]:
    print(pre, v)
    if pre != v:
        if pre == 0:
            s[0] += 1
        else:
            s[1] += 1
        pre = v
    print(s)
print(s)