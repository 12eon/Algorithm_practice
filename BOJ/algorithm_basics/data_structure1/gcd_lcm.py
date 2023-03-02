import sys

def GCD(a,b):
    while b > 0:
        a, b = b, a%b
    return a

def LCM(a,b):
    return a*b // GCD(a,b)

n, m = map(int, sys.stdin.readline().split())
print(GCD(n,m))
print(LCM(n,m))
