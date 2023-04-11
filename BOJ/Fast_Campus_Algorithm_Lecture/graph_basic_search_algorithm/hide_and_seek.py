from collections import deque
MAX = 100001
n,k = map(int, input().split())
v = [0]*MAX

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return v[now]
        for next in (now-1, now+1, now*2):
            if 0 <= next < MAX and not v[next]:
                v[next] = v[now]+1
                q.append(next)
print(bfs())