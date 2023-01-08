length = int(input())
cnt = 0

if length != 1:

    vote = []
    for i in range(length):
        vote.append(int(input()))
        if i == 0:
            goal = vote[-1]

    while max(vote) != goal or vote.count(goal) > 1: # 최고 투표 수인게 2개 이상
        n = vote[1:].index(max(vote))+1 # 1번째가 아닌 후보 중 최고
        if n != 0 or vote.count(goal) > 1:
            vote[0] += 1
            vote[n] -= 1
            goal += 1
            cnt += 1
    print(cnt)
else:
    print(0)