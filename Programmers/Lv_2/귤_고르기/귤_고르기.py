def solution(k, tangerine):
    answer = 0
    dt = {}
    for t in tangerine:
        if t not in dt:
            dt[t] = 1
        else:
            dt[t] += 1

    result = []
    for x in dt.keys():
        result.append(dt[x])
    result.sort(reverse=True)

    i = 0
    while k > 0:
        if result[i] <= k:
            k -= result[i]
            i += 1
            answer += 1
        else:
            answer += 1
            break

    return answer