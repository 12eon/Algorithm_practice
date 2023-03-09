import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

d = [1]*(n+1)
for i in range(1,n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))
