# 효율적인 화폐 구성

n,m = map(int, input().split())
v = [10001]*(m+1) #최대 초과 값
value = []
for _ in range(n):
    x = int(input())
    value.append(x)
    if x < m+1:
        v[x] = 1

for i in range(n):
    for j in range(value[i], m+1): # 가장 작은 단위가 2면
        if v[j-value[i]] != 10001:
            # 자기가 현재 값을 넣을 위치 j
            #j에 들어가기 위해서는 j-2가 10001이 아니여야함
            v[j] = min(v[j], v[j-value[i]]+1)

"""i = 0
while i < m+1:
    while i < m+1:
        if v[i] < 10001:
            break
        i += 1
    for j in range(n):
        dx = i+value[j]
        if dx < m+1:
            v[dx] = min(v[dx], v[i]+1)
        else:
            break
    i += 1"""

if v[m] == 10001:
    print(-1)
else:
    print(v[m])