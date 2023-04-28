import heapq

n = int(input())
cup = []
q = []

for i in range(n):
    a, b = map(int, input().split(' '))
    cup.append((a, b))
cup.sort()

for i in cup:
    a = i[0]
    heapq.heappush(q, i[1])
    if a < len(q):
        heapq.heappop(q)

print(sum(q))