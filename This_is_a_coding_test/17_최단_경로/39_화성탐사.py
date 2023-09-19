import heapq
# 최대, 최소를 빨리 찾아야 하는 경우 != deque : BFS
import math


T = int(input())
for _ in range(T):
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]
    value = [[math.inf for _ in range(N)] for _ in range(N)]
    x = [0,0,1,-1]
    y = [1,-1,0,0]

    q = [[0,0, path[0][0]]]
    value[0][0] = path[0][0]

    while q:
        a, b, c = heapq.heappop(q)
        for i in range(4):
            dx = b + x[i]
            dy = a + y[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            goal = c + path[dy][dx]
            if goal < value[dy][dx]:
                value[dy][dx] = goal
                heapq.heappush(q, [dy, dx, goal])
    print(value[N-1][N-1])