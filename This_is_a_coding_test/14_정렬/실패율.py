def solution(N, stages):
    plist = []
#     stages.sort()
    p = len(stages)
#     j = 0
    for i in range(1, N+1):
        x = 0
#         while (j < len(stages) and stages[j] == i):
#             x += 1
#             j += 1
        x = stages.count(i) # 간단한 풀이
        if x == 0:
            plist.append((0, i))
        else:
            plist.append((x/p, i))
            p -= x
    plist.sort(key = lambda x : (-x[0], x[1]))
    #print(plist)
    return [n[1] for n in plist]

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))