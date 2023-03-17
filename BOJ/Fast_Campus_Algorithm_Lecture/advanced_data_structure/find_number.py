n = int(input())
# 중복된 수 처리
n_value = set(map(int, input().split()))
m = int(input())
m_value = list(map(int, input().split()))

for v in m_value:
    if v in n_value:
        print('1')
    else:
        print('0')