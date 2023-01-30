cmp = [1,1,2,2,2,8]
n = list(input().split())

for i in range(len(n)):
    cmp[i] -= int(n[i])
    print(cmp[i], end =" ")