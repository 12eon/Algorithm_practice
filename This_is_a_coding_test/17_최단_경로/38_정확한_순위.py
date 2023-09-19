import sys

N, M = map(int, input().split())
relation = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relation[a][b] = 1 # a > b: 나보다 작은 것 기록

#플로이드 와샬 알고리즘 : 3중 for문
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if relation[i][k] == 1 and relation[k][j] == 1:
                relation[i][j] = 1 # i > j : 작은 경우만 기록

answer = 0
for i in range(1, N+1):
    small = sum(relation[i])
    tail = sum([1 if relation[j][i] == 1 else 0 for j in range(1, N+1)])
    if (small + tail) == N-1:
        answer += 1
print(answer)