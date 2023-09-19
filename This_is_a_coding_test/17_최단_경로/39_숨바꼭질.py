from collections import deque

N, K = map(int, input().split())
if N > K:
    N,K = K,N
end = max(N, K)*2
dp = [100001 for i in range(end+1)]

q = deque([(N, 1)])
dp[N] = 1
cnt = 0
while q:
    i, pos = q.popleft()
    if i == K:
        break
    for x in (i-1, i+1, i*2):
        if 0 <= x <= end:
            dp[x] = min(dp[x], pos+1)
            q.append([x, pos+1])
print(dp[K])