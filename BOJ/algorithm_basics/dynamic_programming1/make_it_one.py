# 실패
import sys

n = int(sys.stdin.readline())
m = n
result = []

def root(n,x):
    return  int((n)**(1/x))

def calc(n,x):
    r = root(n,x)
    if n%x == 0:
        return r
    return r + (n-r**x)

def check(m):
    i = 0
    while m != 1:
        if m%3 == 0:
            m //= 3
        elif m%2 == 0:
            m //= 2
        else:
            break
        i += 1
    return i, m

for c in range(3):
    i, m = check(n-c)
    if i == 1:
        result.append(i+c)
    result.append(i+calc(m,2))
    result.append(i+calc(m,3))
result.append(calc(n,2))
result.append(calc(n,3))
print(min(result))