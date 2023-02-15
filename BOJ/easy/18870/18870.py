# 시간 초과
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
n_sort = sorted(nums)

result = [-1]*N
i = 0
last = 'x'
while i < N:
    std = n_sort[i]
    cnt = nums.count(std)
    for x in range(cnt):
        d = nums.index(std)
        nums[d] = 'x'
        result[d] = str(i)
    i += cnt

print(' '.join(result))