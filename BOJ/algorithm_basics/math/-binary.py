import sys

n = int(sys.stdin.readline().rstrip())
result = []

while n != 0:
    if n%-2:
        n=n//-2+1
        result.append('1')
    else:
        n//=-2
        result.append('0')
result.reverse()
print(''.join(result))

# 양수처리 실패
"""if n < 0:
    result = ['1']
else:
    result = []
i = 0
while n != 0:
    result.append(str(n%2))
    n //= -2
print(''.join(result))"""