import sys

n = int(sys.stdin.readline().rstrip())
result = []

while n != 0:
    if n%-2: # -2로 나눈 나머지 == -1
        n=n//-2+1
        result.append('1')
    else:
        n//=-2
        result.append('0')
result.reverse()
print(''.join(result))