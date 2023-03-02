import sys

def GCD(a,b):
    while b > 0:
        a, b = b, a%b
    return a

n, s = map(int,sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))

gcd = s-location[0]
for i in range(1,len(location)):
    gcd = GCD(gcd, abs(s-location[i])) # 각 거리들 사이 최대공약수
print(gcd)