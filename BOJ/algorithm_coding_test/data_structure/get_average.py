cnt = int(input())

score = list(map(int, input().split()))
m_score = max(score)
result = 0

# do
""" for s in score:
    result += s/m_score*100
    # 나중에 처리할 수 있는 계산은 최대한 뒤로 미뤄서 최소 처리
print(result/cnt) """

# solve
for s in score:
    result += s
print(result /m_score *100 / cnt)