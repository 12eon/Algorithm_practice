n = int(input())

num = []
num.append([0, 0, 0, 0])
for i in range(n):
    area, height, weight = map(int, input().split())
    num.append((i+1, area, height, weight))

num.sort(key=lambda data: data[-1])

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(0, i):
        if num[i][1] > num[j][1]:
            dp[i] = max(dp[i], dp[j] + num[i][2])

value = max(dp)
cnt = n
result = []
while cnt != 0:
    if value == dp[cnt]:
        result.append(num[cnt][0])
        value -= num[cnt][2]
    cnt -= 1
result.reverse()

print(len(result))
for i in result:
    print(i)
