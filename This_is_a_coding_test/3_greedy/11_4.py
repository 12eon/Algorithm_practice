# 만들 수 없는 금액

d = [0]*(1000001)
n = int(input())
num = list(map(int, input().split()))
num.sort()
nlist = []

def check(j, nlist):
    d[j] = 1
    for i in nlist:
        x = i+j
        if x < len(nlist) and d[x] == 0:
            d[x] = 1
            nlist.append(x)
    if d[j] == 0:
        nlist.append(j)

for i in range(n):
    check(num[i], nlist)

for i in range(1,1000001):
    if d[i] == 0:
        print(i)
        break