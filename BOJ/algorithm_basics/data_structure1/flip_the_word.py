import sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
    value = list(sys.stdin.readline().split())
    for v in value:
        for c in reversed(v):
            print(c, end="")
        print(" ", end="")
    if i != cnt-1:
        print()

'''
cnt = int(sys.stdin.readline())
for i in range(cnt):
    value = list(sys.stdin.readline().split())
    for e in value:
        for i in range(len(e)):
            print(e[-(i+1)], end="")
        print(" ", end="")
    if e != cnt-1:
        print()
'''
