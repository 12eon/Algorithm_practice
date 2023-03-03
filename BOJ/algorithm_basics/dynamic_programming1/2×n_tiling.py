import sys
n = int(sys.stdin.readline())

def h(n,r): # 중복 조합
    #print(n,r)
    return c(n-1+r,r)

def c(n,m): # 조합
    value = 1
    for i in range(m):
        value *= (n-i)
    for j in range(1,m+1):
        value //= j
    return int(value)

result = 1 # 모두 세로
if n%2 == 1: # 홀수
    for x in range(1, n, 2): # 세로
        y = (n-x)//2 # 가로
        result += h(y+1,x)
else: # 짝수
    for x in range(0, n, 2): # 세로
        y = (n-x)//2 # 가로
        result += h(y+1,x)
print(result%10007)
