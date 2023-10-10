import sys
import heapq

input = sys.stdin.readline

n = int(input())
hq = []
for i in list(map(int, input().split())):
    heapq.heappush(hq, i)
min = hq[0]

for _ in range(n-1):
    num = list(map(int, input().split()))
    for i in num:
        if i > min:
            heapq.heappop(hq)
            heapq.heappush(hq, i)
            min = hq[0]
print(hq[0])