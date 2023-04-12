n = int(input())
m = int(input())

com = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    com[x].append(y)
    com[y].append(x)

def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next in com[now_pos]:
        if not visited[next]:
            dfs(next)

dfs(1)
print(count - 1)