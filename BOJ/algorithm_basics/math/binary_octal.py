import sys

def twoToEight(n):
    answer = []
    result = 0
    for i in range(0,len(n),3):
        result = n[i]
        if i+2 < len(n):
            result += n[i+2]*4 + n[i+1]*2
        elif i+1 < len(n):
            result += n[i+1]*2
        answer.append(str(result))
    return ''.join(reversed(answer))


values = list(map(int, sys.stdin.readline().rstrip()))
values.reverse()
print(twoToEight(values))
