import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s1 = []
    s2 = []
    for x in list(input().rstrip()):
        if x == '<':
            if len(s1) > 0:
                s2.append(s1.pop())
        elif x == '>':
            if len(s2) > 0:
                s1.append(s2.pop())
        elif x == '-':
            if len(s1) > 0:
                s1.pop()
        else:
            s1.append(x)
    s2.reverse()
    print(''.join(s1+s2))
