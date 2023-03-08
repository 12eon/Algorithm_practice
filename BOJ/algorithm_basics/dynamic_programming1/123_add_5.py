import sys

m = int(sys.stdin.readline())
num = []
for _ in range(m):
    num.append(int(sys.stdin.readline()))

n = max(num)
dp = []
for _ in range(n+1):
    dp.append([0,0,0]) # 복사 주의
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2])%1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%1000000009

for m in num:
    print(sum(dp[m])%1000000009)