import copy

n = int(input())
for _ in range(n):
    h, w = map(int, input().split())
    #nlist = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
    nlist = list(map(int, input().split()))
    num = []
    for i in range(h):
        num += [nlist[w*i :w*(i+1)]]
    result = copy.deepcopy([x[0] for x in num])
    
    for x in range(1, w):
        for dy in range(h):
            m = 0
            for i in range(-1, 2):
                y = dy + i
                if y < 0 or y >= h:
                    continue
                if m < num[y][x]:
                    m = num[y][x]
            result[dy] += m
    print(max(result))