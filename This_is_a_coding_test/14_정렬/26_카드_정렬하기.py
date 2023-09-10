import heapq # 항상 정렬된 상태
from sys import stdin

cards = []
result = 0

for i in range(int(stdin.readline())):
    heapq.heappush(cards, int(stdin.readline()))

total = 0
while len(cards) > 1:
    value = heapq.heappop(cards) + heapq.heappop(cards)
    total += value
    heapq.heappush(cards, value)
print(total)