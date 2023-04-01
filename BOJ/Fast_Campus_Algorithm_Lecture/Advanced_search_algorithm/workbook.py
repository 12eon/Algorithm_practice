import heapq

n, m = map(int, input().split())
array = [[] for i in range(n + 1)]
degree = [0] * (n + 1)
heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    degree[y] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        degree[y] -= 1
        if degree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')