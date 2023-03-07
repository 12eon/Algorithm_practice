import sys
cnt = int(sys.stdin.readline())

for _ in range(cnt):
    n =  int(sys.stdin.readline())
    d = [0]*(n+1)

    for i in range(1,n+1):
        for j in range(4):
            if j < i:
                d[i] += d[i-j]
        if i < 4:
            d[i] += 1

    print(d[n])