n = int(input())

v = [0 for i in range(n)]
v[0] = 1
i2 = i3 = i5 = 0
next2 = 2
next3 = 3
next5 = 5

i = 1

while v[n-1] == 0:
    v[i] = min(next2, next3, next5)
    
    if v[i] == next2:
        i2 += 1
        next2 = v[i2] * 2
    
    if v[i] == next3:
        i3 += 1
        next3 = v[i3] * 3
    
    if v[i] == next5:
        i5 += 1
        next5 = v[i5] * 5
    i += 1

print(v[n-1])