# 1일 될 때까지

# 나눠질 때까지 -1 or 나머지 없이 나누기
n,k = map(int, input().split())

result = 0
while n > 1:
    r = n%k
    if n >= k: # 최대한 많이 나누기
        n //= k
        result += (r+1)
    else:
        n -= k-1
        result += (k-1)
print(result)