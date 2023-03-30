import heapq
import sys

cnt = int(sys.stdin.readline())
heap = []
result = []

for _ in range(cnt):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap,n)

for data in result:
    print(data)