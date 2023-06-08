# i방문 : (i-1)이 최대한 처리 & 처리가 되는 경우는 answer에 담기
def solution(plans):
    time = []
    plans.sort(key = lambda x :(x[1]))
    for i in range(len(plans)):
        p = plans[i]
        time.append(int(p[2]))
        plans[i][2] = int(p[2])

    answer = []
    pre = [0]
    for i in range(1, len(plans)):
        p = plans[i]
        n = pre[-1]
        h2,s2 = map(int,plans[i][1].split(':'))
        h, s = map(int,plans[n][1].split(':'))
        rest = 60*(h2-h) + (s2-s)
        while len(pre) > 0:
            n = pre[-1]
            if rest >= time[n]:
                rest -= time[n]
                time[n] = 0
                answer.append(plans[n][0])
                pre.pop()
            else:
                time[n] -= rest
                rest = 0
                break
        pre.append(i)
    for p in pre[-1::-1]:
        answer.append(plans[p][0])

    return answer