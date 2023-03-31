import heapq
import sys

num = []
for _ in range(int(sys.stdin.readline())):
    heapq.heappush(num, int(sys.stdin.readline()))
if len(num) == 1:
    print(0)
else:
    while len(num) > 1:
        plus = heapq.heappop(num) + heapq.heappop(num)
        result += plus
        heap.heappush(num, plus)
    print(result)