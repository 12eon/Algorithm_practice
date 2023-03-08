import sys

n = int(sys.stdin.readline())
if n < 3:
    print(1)
else:
    dp = []
    for d in range(n+1):
        dp.append([0,0,0])
    dp[2] = [0,0,1] # 00 01 10

    for i in range(3,n+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][2]
        dp[i][2] = dp[i-1][1]
    print(sum(dp[n]))