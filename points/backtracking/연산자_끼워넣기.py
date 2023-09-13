import sys

def calc(s, p):
    mn = 1000000000
    mx = -1000000000

    def comb(i, now, plus, minus, multiply, divide):
        if i == len(s)-1:
            nonlocal mn, mx
            mn = min(mn, now)
            mx = max(mx, now)
        if plus > 0: # 리스트을 복구 대신 인자 변경
            comb(i+1, now+s[i+1], plus-1, minus, multiply, divide)
        if minus > 0:
            comb(i+1, now-s[i+1], plus, minus-1, multiply, divide)
        if multiply > 0:
            comb(i+1, now*s[i+1], plus, minus, multiply-1, divide)
        if divide > 0:
            if now > 0:
                comb(i+1, now//s[i+1], plus, minus, multiply, divide-1)
            else:
                comb(i+1, -((-now) // s[i + 1]), plus, minus, multiply, divide-1)
    comb(0, s[0], p[0], p[1], p[2], p[3])
    print(mx)
    print(mn)

n = int(sys.stdin.readline())
result = []
s = list(map(int, input().split()))
op = list(map(int, input().split()))
calc(s, op)
