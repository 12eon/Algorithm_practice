n,k = map(int, input().split())

v = [0]*100001
d = [n]
while d != []:
    i = d.pop(0)
    if i == k:
        break
    for j in [i-1, i+1, 2*i]:
        if 0 <= j < 100001 and not v[j]:
        # v[j] > 0 : 이미 전에 계산된 값
            v[j] = v[i]+1
            d.append(j)
print(v[k])
