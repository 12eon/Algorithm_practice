import sys

n = sys.stdin.readline().rstrip()
length = len(n)
if length == 1:
    print(n)
else:
    n = int(n)
    result = 9
    for i in range(2, length):
        cnt = (10**i-1) -(10**(i-1)) +1
        result += cnt*i
    result += (n -10**(length-1) +1)*length
    print(result)