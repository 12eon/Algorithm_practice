# 개미 전사 : 각 단계까지 최고 max 값 누적

n = int(input())
box = list(map(int, input().split()))

v = [0]*(n)
v[0] = box[0]
v[1] = box[1]

for i in range(2, n):
    v[i] = max(v[i-2]+box[i], v[i-1])
    # v[i-1] : 자기가 더해지지 않아도 현재까지 중 최대가 될 수 있음
print(v[n-1])