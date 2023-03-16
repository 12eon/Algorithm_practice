# 데이터 개수가 적기 때문에 append, pop으로 가능
test = int(input())
for _ in range(test):
    cnt, j = map(int, input().split())
    num = list(map(int, input().rstrip().split()))
    n = [(x,i) for i,x in enumerate(num)]

    result = 0
    for _ in range(cnt):
        m = max(n, key=lambda x : x[0])[0]
        while n[0][0] != m:
            n.append(n.pop(0)) # 뒤로
        result += 1
        if n[0][1] == j:
            print(result)
            break
        else:
            n.pop(0)

    """if num.count(pr) == 1:
        result = 0
        for n in num:
             if n > pr:
                result += 1
        print(result+1)
    else:
        d = {} # 개수
        for i in range(cnt):
             if num[i] not in d:
                d[num[i]] = [i]
             else:
                d[num[i]] += [i]
        point = 0 # 다음에 검사할 인덱스
        result = 0
        i = 9
        while i >= pr:
            if i in d:
                if len(d[i]) == 1:
                    point = (d[i][0]%cnt)
                    result += 1
                else:
                    rest = d[i]
                    while len(rest) != 0:
                        #print(rest, point, result)
                        if point in rest:
                            result += 1
                            rest.remove(point)
                            if point == j:
                                break
                        point = (point+1)%(cnt)
            i -= 1
        print(result)"""