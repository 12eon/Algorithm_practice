import sys
def GCD(a,b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(sys.stdin.readline())
for _ in range(n):
    result = 0
    num = list(map(int, sys.stdin.readline().split()))
    length = num.pop(0)
    for i in range(length-1):
        for j in range(i+1, length):
            result += GCD(num[i],num[j])
    print(result)
