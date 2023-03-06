import math
import sys
n = int(sys.stdin.readline())

"""def h(n,r): # 중복 조합
    return c(n-1+r,r)

def c(n,m): # 조합
    value = 1
    for i in range(m):
        value *= (n-i)
    for j in range(1,m+1):
        value //= j
    return int(value)"""

result = 0
for x in range(n%2, n+1, 2): # 1x2
    for x2 in range(0,n-x+1,2): # 2x2
        y = (n-x-x2)//2 # 2x1 개수의 절반
        x_2 = x2//2
        c = math.comb(x_2+y, y)
        h = math.comb(x_2+y+x, x)
        result += c*h
        #result += c(x2//2+y, y)*h(x2//2+y+1, x)
print(result%10007)
