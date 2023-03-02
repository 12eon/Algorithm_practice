import sys
import math

def find_prime(n):
     for i in range(2,int(n**0.5)+1):
         if n%i == 0:
            return 0
     return 1

n, m = map(int, sys.stdin.readline().split())
if n == 1:
    n = 2
for a in range(n,m+1):
    if find_prime(a) == 1:
        print(a)
