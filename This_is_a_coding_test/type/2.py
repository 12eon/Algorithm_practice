# 곱하기 혹은 더하기

n = list(input().rstrip())
n = list(map(int, n))
print(n)

now = n[0]
for i in range(1,len(n)):
    if now <= 1 or n[i] <= 1:
        now += n[i]
    else:
        now *= n[i]
print(now)