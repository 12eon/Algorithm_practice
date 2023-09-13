n, m = map(int, input().split())

def check_next(v, i, max, n):
    if i == max:
        print(' '.join(v))
        return
    for j in range(n):
        if str(j+1) not in v:
            v[i] = str(j+1)
            check_next(v, i+1, max, n)
            v[i] = 0

p = [0 for _ in range(m)]
check_next(p, 0, m, n)